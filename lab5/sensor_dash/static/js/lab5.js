function getData(sensor,count) {

    
        document.getElementById("slidercontainer").style.display="block";
        document.getElementById("loadingMessage").style.display="none";

	fetch('/sensor/'+sensor+'?count='+count).then(response => response.json()).then(
        function(response) { 

            header = document.getElementById('dbheader');
            header.innerHTML = sensor+" Sensor Data";

            table = document.getElementById('data1');
			table.innerHTML = "";
            

                var row = table.insertRow(-1);
		var cell = document.createElement("th");

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

         }
	})
}

function plantInfo() {

  x = document.getElementById("plantWindow");
  if(x.style.display=="none") {
    x.style.display="block";
  }
}


