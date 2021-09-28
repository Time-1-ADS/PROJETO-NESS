var navbarLocation = document.getElementById("navbar").textContent;
var pageTitle = document.title;
var homeElement = document.getElementById("home");
var contactsElement = document.getElementById("contacts");
var dashboardElement = document.getElementById("dashboard");
var registrationElement = document.getElementById("registration");

if (pageTitle == "Main Screen"){
    homeElement.className += " active";
} else if (pageTitle == "Contacts"){
    contactsElement.className += " active";
} else if (pageTitle == "Dashboard"){
    dashboardElement.className += " active";
} else if (pageTitle == "Register"){
    registrationElement.className += " active";
}

function navbar(){
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
}