

var mydata = JSON.parse(data);
var light =[];
var temp_c = [];
var temp_f = [];
var humidity =[];
var sound = [];

var N = 60; 
var n = Array.apply(null, {length: N}).map(Number.call, Number);
//console.log(n);

function load() { 
    
    for ( var n in mydata)
    {
        if(mydata.hasOwnProperty(n))
        {
            light.push(mydata[n].light);
            temp_c.push(mydata[n].celsius);
            temp_f.push(mydata[n].fahrenheit);
            humidity.push(mydata[n].humidity);
            sound.push(mydata[n].envelope);
        }
    }    
    
    
}



$(function () {
    $('#table').bootstrapTable({
        data: Object.values(mydata)
    });
});
