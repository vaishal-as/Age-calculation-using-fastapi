
    function checkform(){
        if(document.getElementById("email").value == ''){
            alert("Required Email");
        }
        else if (document.getElementById("password").value=='' || document.getElementById("password").value<4){
            alert("Password Required and it must be greater than 4");
        }
        else if (document.getElementById("confirm").value==''){
            alert("Please confirm your password");
        }
        else if (document.getElementById("password").value!=document.getElementById("confirm").value){
            alert("Password must match")
            
        }
        else if (document.getElementById("password").value!='' || document.getElementById("email").value!='' || document.getElementById("confirm").value!='' && document.getElementById("password").value==document.getElementById("confirm").value){
            alert("Account was created Successfully")
        }
    }
