var navbarLocation = document.getElementById("navbar").textContent;
var pageTitle = document.title;
var homeElement = document.getElementById("home");
var contactsElement = document.getElementById("contacts");
var dashboardElement = document.getElementById("dashboard");
var registrationElement = document.getElementById("registration");
var leadsElement = document.getElementById("leads");
var profileElement = document.getElementById("profile");

if (pageTitle == "Main Screen" || pageTitle == "Proposta" || pageTitle == "Delete"){
    homeElement.className += " active";
} else if (pageTitle == "Contacts"){
    contactsElement.className += " active";
} else if (pageTitle == "Dashboard"){
    dashboardElement.className += " active";
} else if (pageTitle == "Register" || pageTitle == "Customer Register" || pageTitle == "Employee Register"){
    registrationElement.className += " active";
}
else if (pageTitle == "Leads"){
    leadsElement.className += " active";
}
else if (pageTitle == "Profile"){
    profileElement.className += " active";
}

function navbar(){
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
}