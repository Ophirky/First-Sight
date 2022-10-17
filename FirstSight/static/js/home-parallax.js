// vars
let navbar = document.getElementById("nav-bar");
let sectionOneContainer = document.getElementById("section-1-container");

let registerform = document.getElementById("register-form-link-div");

let signInform = document.getElementById("sign-in-form-section");
let signInSocial = document.querySelector(".form-sign-in-with-social");
let textLoginInputs = document.querySelector(".form-log-in-with-email");

let section2Lines = document.getElementById("lines");
let section2Info = document.getElementById("general-info");
let section2Help = document.getElementById("need-help");

// event listeners
window.addEventListener('scroll', () => {
    var value = window.scrollY;

    if (value > 50) {
        sectionOneContainer.style.opacity = 0;
    } else if (value < 50) {
        sectionOneContainer.style.opacity = 1;
    }

    if (value > 120) {
        navbar.style.backgroundColor = "#0965AE";

    } else if (value < 120) {
        navbar.style.backgroundColor = "rgba(0,0,0,0)";
    }

    if (value > 250) {
        section2Lines.style.opacity = 1;
    } else if (value < 250) {
        section2Lines.style.opacity = 0;
    }

    if (value > 400) {
        section2Info.style.opacity = 1
        section2Help.style.opacity = 1

    } else if (value < 400) {
        section2Info.style.opacity = 0
        section2Help.style.opacity = 0
    }

    if (value > 920) {
        registerform.style.opacity = 1;
    } else if (value < 920) {
        registerform.style.opacity = 0;
    }

    if (value > 1410) {
        textLoginInputs.style.opacity = 1;
        signInSocial.style.opacity = 1;
    } else if (value < 1410) {
        textLoginInputs.style.opacity = 0;
        signInSocial.style.opacity = 0;
    }

    console.log(value);
})