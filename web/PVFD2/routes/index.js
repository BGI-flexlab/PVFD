/* GET home page. */
exports.index = function(req, res){
  res.render('index', { title: 'Express' });
};

exports.data = function(req,res){
  res.render('freq',{title:'Frequency',value:req.param("value")});
};

exports.faq = function(req,res){
  res.render('faq',{title:'FAQ'});
};

exports.stat = function(feq,res){
  res.render('stat',{title:'Statistics'});
};

exports.about = function(req,res){
  res.render('about',{});
};
