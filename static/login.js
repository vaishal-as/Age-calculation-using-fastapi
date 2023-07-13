function redirect(){
    if(document.getElementById("en").value == ''){
        alert("Required Email");
    }
    else if (document.getElementById("pn").value=='' || document.getElementById("pn").value<4){
        alert("Password Required and it must be greater than 4");
    }
    else if (document.getElementById("pn").value!='' || document.getElementById("pn").value!=''){
        alert("Login Successfull")
    }

}