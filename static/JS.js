var Green_displayer =document.getElementById("result")
var total_shower=document.getElementById("total");
var total=0;
var counter = 2;
var submition = document.getElementById("Submition");
submition.addEventListener("click", function(event) {
    event.preventDefault();
    var Product = document.getElementById("product").value;
    var Description = document.getElementById("description").value;
    var Size = document.getElementById("Size_product").value;
    adder.classList.add("success");
    adder.classList.add("Bold");
    if(total<150){
    Green_displayer.style.display="block";
}
else{
    Green_displayer.style.display="block";
    Green_displayer.style.color= "red";
    Green_displayer.innerHTML="Poor job! Your Purchases are environmentally harmful."

}
    document.getElementById("product").value = "";
    document.getElementById("description").value = "";
    document.getElementById("Size_product").value = "";

    fetch("http://127.0.0.1:8000/posts", {
        method: "POST",
        body: JSON.stringify({

        "name": Product,
        "material": Description,
        "size": Size
      }),
  headers: {
    "Content-type": "application/json; charset=UTF-8"
  }
});





    var adder = document.getElementById("MyTable").insertRow(counter);
    adder.classList.add("success");
    if(!Product || !Description || !Size){
        alert("Please enter all the required fields");
        return;
    }
    adder.insertCell(0).innerHTML = Product;
    adder.insertCell(1).innerHTML = Description;
    adder.insertCell(2).innerHTML = Size;
    
if(total<150){
    Green_displayer.style.display="block";
}
else{
    Green_displayer.style.display="block";
    Green_displayer.style.color= "red";
    Green_displayer.innerHTML="Poor job! Your Purchases are environmentally harmful."

}

})

window.onload= ()=>{
    fetch('http://127.0.0.1:8000/load')
        .then(res => res.json())
        .then(data => {console.log(data)})
        
};


