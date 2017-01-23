/**
 * Created by Administrator on 2016/10/13.
 */

function isEmpty(data){
    if (data == null || data == ""){
        return true;
    }else{
        return false;
    }
}

function dealJsonStr(data,source,label){
    var json = JSON.parse(data);
    for (var key in json){
        label.push(key);
        var obj = json[key];
        var genotypeCount = obj["totalGenotypeCount"];
        var temp = {};
        temp['name'] = key;
        temp['value'] = genotypeCount;
        source.push(temp);
    }
    label = label.sort();
}

function dealTotalMAF(data){
    var json = JSON.parse(data);
    var alleles = json["alleles"];
    var freqArr = [];
    //console.log(JSON.stringify(alleles,2,2));
    for (var key in alleles){
        var obj = alleles[key];
        var freq = obj["frequency"];
        freqArr.push(freq);
    }
    if (freqArr.length == 1){
        return 1;
    }else if (freqArr.length >1){
        var sortArr = freqArr.sort(sortFun);
        return sortArr[1];
    }else{//error
        return 0;
    }
}

function dealPopMAF(data,source,label){
    var json = JSON.parse(data);
    for (var pop in json){
        var obj = json[pop];
        var alleles = obj["alleles"];
        var freqArr = [];
        for (var base in alleles){
            var values = alleles[base];
            var freq = values["frequency"];
            freqArr.push(freq);
        }
        if (freqArr.length >1){
            //console.log(JSON.stringify(freqArr,2,2));
            var sortArr = freqArr.sort(sortFun);
            //console.log(JSON.stringify(freqArr,2,2));
            label.push(pop);
            var tmp = {};
            tmp['name'] = pop;
            tmp['value'] = sortArr[1]*100;
            source.push(tmp);
        }
    }
    label = label.sort();
}

function dealAlleleCount(ref,data,source1,source2,label){
    var json = JSON.parse(data);
    var tmp1 = {};
    var tmp2 = {};
    for (var key in json){
        label.push(key);
        var obj = json[key];
        var alleleNumber = obj["totalAlleleCount"];
        var alleles = obj["alleles"];
        var alleleRef = alleles[ref];;
        var alleleCount = alleleRef["count"];
        tmp1[key] = alleleCount;
        tmp2[key] = alleleCount/alleleNumber;
    }
    label = label.sort();
    label.forEach(function(lab){
        source1.push(tmp1[lab]);
        source2.push(tmp2[lab]*100);
    });
}


function sortFun(a,b){
    return b-a;
}

String.prototype.startWith=function(str){
    var reg=new RegExp("^"+str);
    return reg.test(this);
}

String.prototype.endWith=function(str){
    var reg=new RegExp(str+"$");
    return reg.test(this);
}