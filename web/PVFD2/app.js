var express = require('express');
var http = require('http');
var path = require('path');
var favicon = require('static-favicon');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');
var ejs = require('ejs');
var routes = require('./routes');
var users = require('./routes/user');

var app = express();

// view engine setup
app.set('port', process.env.PORT || 8084);
app.set('views', __dirname + '/views');
app.engine('.html', ejs.__express);
app.set('view engine', 'html');
app.use(express.favicon());
app.use(express.logger('dev'));
app.use(express.bodyParser());
//app.use(express.json());
//app.use(express.urlencoded());
//app.use(bodyParser.json());
app.use(cookieParser('mySecret'));
app.use(express.session());
app.use(express.methodOverride());
app.use(app.router);
app.use(express.static(path.join(__dirname, 'public')));;

app.get('/', routes.index);
app.get('/data/:value',routes.data);
app.get('/faq',routes.faq);
app.get('/stat',routes.stat);
app.get('/about',routes.about);


//rest api
app.post("/findByKeyWord",function(req,resq){
    //console.log(JSON.stringify(req));
    var query = req.body.q;
    var bundle = "json="+JSON.stringify({q:query});
    console.log(bundle);
    var options = {
        //host: '192.168.3.155',
        host: 'localhost',
        port: 8080,
        path: '/PVFD2RestServer_V1.0/service/freq/findByKeyWord',
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
    };
    var req = http.request(options, function(res) {
        console.log('STATUS: ' + res.statusCode);
        //console.log('HEADERS: ' + JSON.stringify(res.headers));
        res.setEncoding('utf8');
        var resultString = "";
        res.on('data', function (chunk) {
            resultString += chunk;
        });
        res.on('end',function(){
            var rs_json = JSON.parse(resultString);
            if (rs_json.code == 1){//success
                //resq.send(rs_json);
            }else{//error

            }
            resq.send(rs_json);
        });

    });

    req.on('error', function(e) {
        console.log('problem with request: ' + e.message);
    });

// write data to request body
    req.write(bundle);
    req.end();
});

app.get("/sampleCount",function(req,resq){
    var options = {
        host: 'localhost',
        port: 8080,
        path: '/PVFD2RestServer_V1.0/service/sample/getSampleCount',
        method: 'GET',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
    };
    var req = http.request(options, function(res) {
        console.log('STATUS: ' + res.statusCode);
        //console.log('HEADERS: ' + JSON.stringify(res.headers));
        res.setEncoding('utf8');
        var resultString = "";
        res.on('data', function (chunk) {
            resultString += chunk;
        });
        res.on('end',function(){
            var rs_json = JSON.parse(resultString);
            if (rs_json.code == 1){//success
                //resq.send(rs_json);
            }else{//error

            }
            resq.send(rs_json);
        });

    });

    req.on('error', function(e) {
        console.log('problem with request: ' + e.message);
    });

// write data to request body
//    req.write(bundle);
    req.end();
});


/// catch 404 and forwarding to error handler
app.use(function(req, res, next) {
    var err = new Error('Not Found');
    err.status = 404;
    next(err);
});

/// error handlers

// development error handler
// will print stacktrace
if (app.get('env') === 'development') {
    app.use(function(err, req, res, next) {
        res.render('error', {
            message: err.message,
            error: err
        });
    });
}

// production error handler
// no stacktraces leaked to user
app.use(function(err, req, res, next) {
    res.render('error', {
        message: err.message,
        error: {}
    });
});


http.createServer(app,function(req,res){
    if(req.url === '/favicon.ico') {
        console.log('Favicon was requested');
    }
}).listen(app.get('port'), function() {
    console.log('Express server listening on port ' + app.get('port'));
});

