function getSelected() {
    //Reference the Table.
    var asg_name = document.getElementById("asg").value;
    if (asg_name == "") {
        alert("Asg name cannot be empty")
    } else {
        var grid = document.getElementById("promptInfo");
        //Reference the CheckBoxes in Table.
        var checkBoxes = grid.getElementsByTagName("INPUT");
        var message = "";
        //Loop through the CheckBoxes.
        for (var i = 0; i < checkBoxes.length; i++) {
            if (checkBoxes[i].checked) {
                var row = checkBoxes[i].parentNode.parentNode;
                message += row.cells[0].innerHTML;
                message += ",";
                // message += "   " + row.cells[2].innerHTML;
                // message += "   " + row.cells[3].innerHTML;
                // message += "\n";
            }
        }
        console.log(message);
        const data_sent = message.slice(0, -1) //
        console.log(data_sent.length);
        l = Array.from(data_sent);
        console.log(l);
        //Display selected Row data in Alert Box.
        //alert(data_sent);

        if (  (data_sent.length > 7))  {
            if(data_sent.length == 8)
            {
                   const xhttp = new XMLHttpRequest();
            const method = "POST";
            const async = true;
            const url = window.location.href;
            xhttp.open(method, url, async);
            xhttp.setRequestHeader("Content-Type", "application/json");
            xhttp.onload = function () {

            }
            var prompts = data_sent.split(",")
            xhttp.send(JSON.stringify({"asg_name": asg_name, "prompts": prompts}));

            }
            else {
                alert("You can only select 4 prompts");
            }
        } else {
            //get data to send to the server

            const xhttp = new XMLHttpRequest();
            const method = "POST";
            const async = true;
            const url = window.location.href;
            xhttp.open(method, url, async);
            xhttp.setRequestHeader("Content-Type", "application/json");
            xhttp.onload = function () {

            }
            var prompts = data_sent.split(",")
            xhttp.send(JSON.stringify({"asg_name": asg_name, "prompts": prompts}));


        }


    }
}