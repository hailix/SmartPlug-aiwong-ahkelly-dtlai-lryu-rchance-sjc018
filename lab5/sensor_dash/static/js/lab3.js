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


function getData(name) {
        
// pulled this off of my homework, not quite right for this
	fetch('/sensor/'+name).then(response => response.json()).then(function(response) { for (var key in response) {
		console.log(key)
		if(key != "id") {
			document.getElementById(key).innerHTML=response[key]
	        }
	}
	})
}


$(function () {
    $('#table').bootstrapTable({
        data: Object.values(mydata)
    });
});
