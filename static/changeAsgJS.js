function changeAsg(element)
{

        //var new_group = element.parentElement.parentElement.cells[8].querySelector("#group").value;
        //var group=0;
        //group = document.getElementById("group").value;
        //var g = $('#group:selected').val();
        //var patient_id = element.parentElement.parentElement.cells[0].innerHTML;
       //var group_name = element.parentElement.parentElement.cells[8].value;
         //var p_status = $('.state :selected').val();
         var new_group = element.parentElement.parentElement.cells[8].querySelector("#group").value;
          var patient_id = element.parentElement.parentElement.cells[0].innerHTML;
        console.log(patient_id);
        console.log(new_group);
         const xhttp = new XMLHttpRequest();
     const method = "PUT";
     const async = true;
     const url = window.location.href;
     xhttp.open(method, url, async);
     xhttp.setRequestHeader("Content-Type", "application/json");
    	xhttp.onload = function() {

    }

    xhttp.send(JSON.stringify({"patient_id":patient_id,"group_id":new_group}));

    clear();


}

function clear()
{
    alert("Changes done")
}