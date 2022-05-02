
document.getElementById("enter").disabled=true;

function check_checkbox(){

if (document.getElementById("terms").checked)
{
    document.getElementById("enter").disabled=false;
}
else{
    document.getElementById("enter").disabled=true;
}
}