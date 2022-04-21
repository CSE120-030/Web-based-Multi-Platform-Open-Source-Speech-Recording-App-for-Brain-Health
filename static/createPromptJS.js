function checkForm()
{
var image = document.getElementById("imageSelected");

if(image.files.length==0)
{
    alert("No Image has been selected")
    if(confirm("Submit prompt?"))
    {
        //no image for the prompt
        //send data to server
    var description = document.getElementById("text_description").value;
    var type_of_prompt = document.getElementById("type_of_prompt").value;
    var type_of_language = document.getElementById("type_of_language").value;
    var image =9
         const xhttp = new XMLHttpRequest();
     const method = "POST";
     const async = true;
     const url = window.location.href;
     xhttp.open(method, url, async);
     xhttp.setRequestHeader("Content-Type", "application/json");
     xhttp.onload = function() {



    }
    xhttp.send(JSON.stringify({"prompt_description": description, "type_of_prompt": type_of_prompt,"type_of_language":type_of_language,
    "image_name":image}));

    }
    else{

    }
}
else{
    //send data to server
    var description = document.getElementById("text_description").value;
    var type_of_prompt = document.getElementById("type_of_prompt").value;
    var type_of_language = document.getElementById("type_of_language").value;
    var imageSelected = document.getElementById("imageSelected");
    var imageName = imageSelected.files.item(0).name; //get name of picture chosen
    console.log(imageName);
    console.log(description);
    console.log(type_of_prompt);
    console.log(type_of_language);
    console.log(window.location.href);
    const xhttp = new XMLHttpRequest();
     const method = "POST";
     const async = true;
     const url = window.location.href;
     xhttp.open(method, url, async);
     xhttp.setRequestHeader("Content-Type", "application/json");
    	xhttp.onload = function() {



    }
    xhttp.send(JSON.stringify({"prompt_description": description, "type_of_prompt": type_of_prompt,"type_of_language":type_of_language,
    "image_name":imageName}));

}

}