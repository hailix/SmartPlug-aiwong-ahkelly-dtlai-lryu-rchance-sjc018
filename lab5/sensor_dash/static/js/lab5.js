function getData(sensor,count) {
 //console.log(count);     
        document.getElementById("slidercontainer").style.display="block";
// pulled this off of my homework, not quite right for this
	fetch('/sensor/'+sensor+'?count='+count).then(response => response.json()).then(
        function(response) { 

            header = document.getElementById('dbheader');
            header.innerHTML = sensor+" Sensor Data";

            table = document.getElementById('data1');
			table.innerHTML = "";
            

             	//var row = document.createElement("tr");
                var row = table.insertRow(-1);
		var cell = document.createElement("td");

                if (sensor == "MCP") {
                  row.insertCell(-1).innerHTML="Voltage Level";
                  table.appendChild(row);	      
	        }

                else if(sensor == "DHT") {
                  row.insertCell(-1).innerHTML="Degrees Celsius";
                  row.insertCell(-1).innerHTML="Degrees Fahrenheit";
                  row.insertCell(-1).innerHTML="Humidity";
                  table.appendChild(row);
                }     

                else if(sensor == "SS") {
                  row.insertCell(-1).innerHTML="Audio Signal";
                  row.insertCell(-1).innerHTML="Audio Envelope";
                  row.insertCell(-1).innerHTML="Audio Gate";
                  table.appendChild(row);
                }



            for (var item in response["tmp"]) {
              
        console.log(response["tmp"]);
  //      console.log(item);
     //   console.log(value);
     //   console.log(typeof(value));
    //    console.log(response["tmp"][0].celsius);
        row = document.createElement("tr");
        cell1 = document.createElement("td");

        if(sensor == "MCP") {
	  value = document.createTextNode(response["tmp"][item].voltage);
          cell1.appendChild(value);
          row.appendChild(cell1);
          table.appendChild(row);
                        
	}
        if(sensor == "DHT") {
          row.insertCell(-1).innerHTML=response["tmp"][item].celsius;
          row.insertCell(-1).innerHTML=response["tmp"][item].fahrenheit;
          row.insertCell(-1).innerHTML=response["tmp"][item].humidity;
          table.appendChild(row);
	}
        if(sensor == "SS") {
          row.insertCell(-1).innerHTML=response["tmp"][item].audio;
          row.insertCell(-1).innerHTML=response["tmp"][item].envelope;
          row.insertCell(-1).innerHTML=response["tmp"][item].gate;
          table.appendChild(row);
	}
      //  cell1.appendChild(value);
      //  row.appendChild(cell1);
      //  table.appendChild(row);
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

