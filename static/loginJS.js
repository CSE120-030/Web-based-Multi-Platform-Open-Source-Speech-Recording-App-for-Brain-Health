function logIn()
{
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    const xhttp = new XMLHttpRequest();
	const method = "POST";
	const async = true;
	const url = window.location.href + "login";
	console.log(url);
    xhttp.open(method, url, async);
	xhttp.setRequestHeader("Content-Type", "application/json");

    xhttp.onload = function() {
    if (xhttp.status == 404) {
			const error = document.createElement("P");
			error.className = "error";
			let text = document.createTextNode("Username not found");
			error.appendChild(text);
			document.getElementById("form_block").appendChild(error);
		}
    else if (xhttp.status == 409) {
			const error = document.createElement("P");
			error.className = "error";
			let text = document.createTextNode("Password Incorrect");
			error.appendChild(text);
			document.getElementById("form_block").appendChild(error);
		}
    else {
			location.reload()
		}

    }
        xhttp.send(JSON.stringify({"username": username, "password": password}));

}
function clear_errors() {
	const errors = document.getElementsByClassName("error");
	for (var i = 0; i < errors.length; i++) {
		errors[i].remove();
	}
}
