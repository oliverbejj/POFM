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


    
    if(Description=="Plastics"){
        if(Size=="Medium"){
            adder.insertCell(3).innerHTML = 4;
            total+=4;
        }
        else if(Size=="Large"){
            adder.insertCell(3).innerHTML = 4*(1.5);
            total+=4*(1.5)
        }
        else if(Size=="Small"){
            adder.insertCell(3).innerHTML = 4*(0.5);
            total+=4*(0.5)
        }
    }
    else if(Description=="Glass"){
        if(Size=="Small"){
            adder.insertCell(3).innerHTML = 0.5;
            total+=0.5
        }
        else if(Size=="Medium"){
            adder.insertCell(3).innerHTML = 1;
            total+=1
        }
        else if(Size=="Large"){
            adder.insertCell(3).innerHTML = 1.5;
            total+=1.5
        }
    }
    else if(Description=="Paper"){
        if(Size=="Small"){
            adder.insertCell(3).innerHTML = 3*0.5;
            total+=(3*0.5)
        }
        else if(Size=="Medium"){
            adder.insertCell(3).innerHTML = 3;
            total+=3
        }
        else if(Size=="Large"){
            adder.insertCell(3).innerHTML = 3*1.5;
            total+=3*1.5
        }
    }
    else if(Description=="Aluminium"){
        if(Size=="Small"){
            adder.insertCell(3).innerHTML = 0.5;
            total+=0.5
        }
        else if(Size=="Medium"){
            adder.insertCell(3).innerHTML = 1;
            total+=1
        }
        else if(Size=="Large"){
            adder.insertCell(3).innerHTML = 1.5;
            total+=1.5
        }
    }
    else if(Description=="Foils and laminates"){
        if(Size=="Small"){
            adder.insertCell(3).innerHTML = 4*0.5;
            total+=0.5*4
        }
        else if(Size=="Medium"){
            adder.insertCell(3).innerHTML = 1*4;
            total+=1*4
        }
        else if(Size=="Large"){
            adder.insertCell(3).innerHTML = 1.5*4;
            total+=1.5*4
        }
    }
    else if(Description=="Tinplate"){
        if(Size=="Small"){
            adder.insertCell(3).innerHTML = 2*0.5;
            total+=0.5*2
        }
        else if(Size=="Medium"){
            adder.insertCell(3).innerHTML = 1*2;
            total+=1*2
        }
        else if(Size=="Large"){
            adder.insertCell(3).innerHTML = 1.5*2;
            total+=1.5*2
        }
    }
    else if(Description=="Tin-Free steel"){
        if(Size=="Small"){
            adder.insertCell(3).innerHTML = 3*0.5;
            total+=0.5*3
        }
        else if(Size=="Medium"){
            adder.insertCell(3).innerHTML = 3*1;
            total+=1*3
        }
        else if(Size=="Large"){
            adder.insertCell(3).innerHTML = 3*1.5;
            total+=1.5*3
        }
    }
    else if(Description=="Paperboards"){
        if(Size=="Small"){
            adder.insertCell(3).innerHTML = 0.5*4;
            total+=0.5*4
        }
        else if(Size=="Medium"){
            adder.insertCell(3).innerHTML = 1*4;
            total+=1*4
        }
        else if(Size=="Large"){
            adder.insertCell(3).innerHTML = 1.5*4;
            total+=1.5*4
        }
    }
    total_shower.innerHTML = total
    counter++;

if(total<150){
    Green_displayer.style.display="block";
}
else{
    Green_displayer.style.display="block";
    Green_displayer.style.color= "red";
    Green_displayer.innerHTML="Poor job! Your Purchases are environmentally harmful."

}

})


