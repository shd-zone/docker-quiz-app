document.addEventListener("DOMContentLoaded", function () {

    // Welcome alert
    console.log("Welcome to Flirty Quiz ❤️");

    // Button click animation
    const button = document.querySelector(".start-btn");

    if (button) {
        button.addEventListener("click", function () {
            button.innerHTML = "Loading... 💕";
        });
    }

    // Hover effect
    if (button) {
        button.addEventListener("mouseover", function () {
            button.style.transform = "scale(1.08)";
        });

        button.addEventListener("mouseout", function () {
            button.style.transform = "scale(1)";
        });
    }

});