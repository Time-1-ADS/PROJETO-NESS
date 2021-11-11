var email = document.getElementById("email").value
var error = document.getElementById("error")

function login(){
    if (email == "admin@admin.com"){
        email.addEventListener("click", function(){
            window.open("/", "_blank")
        })
    }else{
        error.className = " "
    }
}