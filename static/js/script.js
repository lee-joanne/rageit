let signUpMessage = document.getElementById("signup-message")
let signUpHover = document.getElementById("signup-hover")

signUpHover.addEventListener("mouseover", showMessage);
signUpHover.addEventListener("mouseout", hideMessage);

function showMessage() {
    /*
    Function to preview sign up message in Sign Up html page when user hovers mouse over arrow
    */
    signUpMessage.classList.remove("hide");
}

function hideMessage() {
    /*
    Function to hide sign up message in Sign Up html page when user removes mouse over arrow
    */
    signUpMessage.classList.add("hide");
}

function postSuccessMessage() {
    let postSuccess = document.getElementById("success-post-alert")
    postSuccess.classList.remove("hide")
}