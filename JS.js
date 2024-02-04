var counter =3;
var submition = document.getElementById("Submition");
submition.addEventListener("click",addToTable);
function addToTable(){
    console.log(4)
    event.preventDefault();
    var Product= document.getElementById("product").value;
    var Description= document.getElementById("description").value;
    var Size= document.getElementById("Size_product").value;
    console.log(Size)
    let adder =document.getElementById("MyTable");
    console.log(document.getElementById("MyTable"))
    console.log(adder)
    adder.insertRow(counter);
    adder.insertCell(0).innerHTML= Product;
    adder.insertCell(1).innerHTML= Description;
    adder.insertCell(2).innerHTML= Size;
    counter++;
    window.location.href="index.html";
}
