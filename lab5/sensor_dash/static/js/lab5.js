function getData(sensor,count) {

        document.getElementById("slidervalue").innerHTML = count;
        document.getElementById("slidercontainer").style.display="block";
        document.getElementById("loadingMessage").style.display="none";
        document.getElementById("disclaimer").style.display="block";

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
                  row.insertCell(-1).innerHTML="Approximate % of Light";
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

          row.insertCell(-1).innerHTML=response["tmp"][item].voltage;
          x = row.insertCell(-1);
          x.innerHTML=(Number(response["tmp"][item].voltage)*.101317-3.04);
         
          if(Number(x.innerHTML) < 40) {
            x.style.color = "red";
          } 
         
          table.appendChild(row);
                        
	}
        if(sensor == "DHT") {
          x = row.insertCell(-1);
          x.innerHTML=response["tmp"][item].celsius;
          
          if(Number(x.innerHTML) > 28) {
            x.style.color ="red";
          }
          x = row.insertCell(-1);
          x.innerHTML=response["tmp"][item].fahrenheit;

          if(Number(x.innerHTML) > 82) {
            x.style.color="red";
          }
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

var slider = document.getElementById("slidebar");
var output = document.getElementById("slidervalue");

slider.oninput = function() {
  output.innerHTML = this.value;
}

