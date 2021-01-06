   // api url 
const api_url =  
      "https://prodapi.metweb.ie/weather/short/Dublin"; 
  
// Defining async function 
async function getapi(url) { 
    
    // Storing response 
    const response = await fetch(url); 
    
    // Storing data in form of JSON 
    var data = await response.json(); 
    console.log(data); 
    if (response) { 
        hideloader(); 
    } 
    show(data); 
} 
// Calling that async function 
getapi(api_url); 
  
// Function to hide the loader 
function hideloader() { 
    document.getElementById('loading').style.display = 'none'; 
} 
// Function to define innerHTML for HTML table 
function show(data) { 
    let tab =  
        `<tr> 
          <th>Location</th> 
          <th>Temperature</th> 
          <th>Humidity</th> 
          <th>Pressure</th> 
          <th>Rainfall</th> 
  		  <th>Warning</th> 
          <th>Weather Description</th> 
          <th>Wind Speed</th>   
         </tr>`; 
    
    // Loop to access all rows  
    for (let r of data.list) { 
        tab += `<tr>  
    <td>${r.station} </td> 
    <td>${r.temperature}</td> 
    <td>${r.humidity}</td>  
    <td>${r.pressure}</td>   
    <td>${r.rainfall}</td>  
    <td>${r.temperatureClass}</td> 
    <td>${r.weatherDescription}</td>  
    <td>${r.windSpeed}</td>         
</tr>`; 
    } 
    // Setting innerHTML as tab variable 
    document.getElementById("meteo").innerHTML = tab; 
} 