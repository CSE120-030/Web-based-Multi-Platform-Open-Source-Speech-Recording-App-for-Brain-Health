function startAsg(groupName)
{
group_name = groupName.parentElement.parentElement.cells[0].innerHTML;
console.log(group_name);
const xhttp = new XMLHttpRequest();
     const method = "POST";
     const async = true;
     const url = window.location.href;
     xhttp.open(method, url, async);
     xhttp.setRequestHeader("Content-Type", "application/json");
     xhttp.onload = function() {



    }
    xhttp.send(JSON.stringify({"group_name":group_name}));

}