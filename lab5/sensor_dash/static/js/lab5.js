function getData(sensor,count) {
 //console.log(count);     
// pulled this off of my homework, not quite right for this
	fetch('/sensor/'+sensor+'?count='+count).then(response => response.json()).then(
        function(response) { 
            table = document.getElementById('data1');
            for (var item in response["tmp"]) {
              
        console.log(response["tmp"]);
        console.log(item);
     //   console.log(value);
     //   console.log(typeof(value));
        console.log(response["tmp"][0].celsius);
        row = document.createElement("tr");
        cell1 = document.createElement("td");
        cell2 = document.createElement("td");
        value = document.createTextNode(response["tmp"][0].celsius);
        cell1.appendChild(value);
        row.appendChild(cell1);
        table.appendChild(row);
        //document.getElementById('data1').innerHTML=response["tmp"][0].celsius; 
	       
         }
	})
}

var clicked1 = function(name, count) {
    console.log('hi');
  fetch('/sensor/'+name+'?count='+count)
    .then(response => response.json())
    .then(function(response) {
      // document.getElementById('bn').innerHTML=response['business_name'];
      // document.getElementById('bt').innerHTML=response['business_type'];
      // document.getElementById('mt').innerHTML=response['market_type'];
      // document.getElementById('jd').innerHTML=response['job_to_be_done']
      // document.getElementById('rm').innerHTML=response['revenue_model'];
      
      for (item in response) {
        
        document.createElement(item).item(0);
        document.getElementById('data1').innerHTML=response['tmp'][0];
      }
    }
  );
}

