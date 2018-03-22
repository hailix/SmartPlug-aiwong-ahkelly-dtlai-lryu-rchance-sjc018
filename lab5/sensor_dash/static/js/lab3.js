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
 console.log('hi');     
// pulled this off of my homework, not quite right for this
	fetch('/'+name).then(response => response.json()).then(
        function(response) { 
            for (item in response) {
                for (var key in item) {
		          console.log(key)
		          if(key != "id") {
			         document.getElementById(key).innerHTML=item[key];
            }
	        }
	   }
	})
}

var clicked1 = function(name, count) {
    console.log('hi');
  fetch('http://localhost:5050/sensor/'+name+'?count='+count)
    .then(response => response.json())
    .then(function(response) {
      // document.getElementById('bn').innerHTML=response['business_name'];
      // document.getElementById('bt').innerHTML=response['business_type'];
      // document.getElementById('mt').innerHTML=response['market_type'];
      // document.getElementById('jd').innerHTML=response['job_to_be_done']
      // document.getElementById('rm').innerHTML=response['revenue_model'];
      for (item in response) {
        document.getElementById('data1').innerHTML=response['tmp'];
      }
    }
  );


$(function () {
    $('#table').bootstrapTable({
        data: Object.values(mydata)
    });
});
