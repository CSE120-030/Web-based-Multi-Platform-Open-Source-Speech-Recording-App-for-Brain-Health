function sendData()
{
    alert("button clicked");

    //get data
    var fist_name = document.getElementById("first_name").value;
    var last_name = document.getElementById("last_name").value;
    var type_of_language = document.getElementById("type_of_language").value;
    var email = document.getElementById("e").value;
    var username = document.getElementById("user_name").value;
    var password = document.getElementById("password").value;
    var dob = document.getElementById("dob").value;
    var sex = document.getElementById("sex").value;

    console.log(fist_name,last_name,type_of_language,email,username,password,dob,sex);
        const xhttp = new XMLHttpRequest();
     const method = "POST";
     const async = true;
     const url = window.location.href;
     xhttp.open(method, url, async);
     xhttp.setRequestHeader("Content-Type", "application/json");
    	xhttp.onload = function() {



    }
    xhttp.send(JSON.stringify({"first_name": fist_name, "last_name":last_name,"language":type_of_language,
    "email":email, "user_name":username,"password":password,"dob":dob,"sex":sex}));
        alert("Data submitted");
        clear();





}
function clear()
{
     document.getElementById("first_name").value="";
      document.getElementById("last_name").value="";
      document.getElementById("e").value="";
     document.getElementById("user_name").value="";
     document.getElementById("password").value="";
    document.getElementById("dob").value ="";
    //fist_name="";
    //last_name="";
    //username="";
    //password="";
    //dob="";
}