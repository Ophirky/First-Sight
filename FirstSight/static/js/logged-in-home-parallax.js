// vars
let navbar = document.getElementById("nav-bar");
// event listeners
window.addEventListener('scroll', () => {
    var value = window.scrollY;

    if (value > 120) {
        // navbar.style.backgroundColor = "#0965AE";

    } else if (value < 120) {
        // navbar.style.backgroundColor = "rgba(0,0,0,0)";
    }

    console.log(value);
})