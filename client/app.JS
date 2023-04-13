function getBathValue() {
  var uiBathrooms = document.getElementsByName("uiBathrooms");
  for(var i in uiBathrooms) {
    if(uiBathrooms[i].checked) {
        return parseInt(i);
    }
  }
  return -1; // Invalid Value
}

function getWheelValue() {
 
  const selected = document.querySelector('input[name="uiWheelChair"]:checked').value;
 
  return selected
}

function getParkingValue() {
  const selected = document.querySelector('input[name="uiParking"]:checked').value;

  return selected

  
}

function getPetValue() {
 
  const selected = document.querySelector('input[name="uiPetsallowed"]:checked').value;

  return selected
}


function getTotalRoom() {

  const selected = document.querySelector('input[name="uirooms"]:checked').value;

  return selected
  
}

function getPowerValue() {
  const selected = document.querySelector('input[name="uiPowerBackup"]:checked').value;

  return selected
}



function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  
  var power = getPowerValue();
  var wheel = getWheelValue();
  var pet = getPetValue();
  var room = getTotalRoom();
  var park = getParkingValue();
  var bathrooms = getBathValue()+1;
  var floor = 3;

  var sqft = document.getElementById("uiSqft");
  
  

  var furnishing = document.getElementById("uifurnishing");

  var available_for = document.getElementById("uiavailablefor");

  var property_age = document.getElementById("uipptyage");

  var floor_type = document.getElementById("uifloor_type");
  
  var estPrice = document.getElementById("uiEstimatedPrice");

  var place =document.getElementById("uiplace");


  var url = "http://127.0.0.1:5000/predict_rent_amount";





  $.post(url, {
      place: place.value,
      bathroom: bathrooms,
      area: parseFloat(sqft.value),
      floor_number:floor,
      parking:park,
      
      power_backup:power,
     
      total_rooms:room,
      furnishing: furnishing.value,
      available_for: available_for.value,
      property_age: property_age.value,
      wheelchairavailability:wheel,
      pets_allowed:pet,
      floor_type:floor_type.value

  
  },function(data, status) {
      
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " rupees ";
      console.log(status);
  });
}

