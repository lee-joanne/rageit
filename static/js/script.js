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

function imageValidate() {
    /*
    Function to ensure images match jpeg, jpg, or png before submission.
    Inspired by code from https://stackoverflow.com/questions/8053394/how-to-do-something-before-on-submit
    as well as: https://stackoverflow.com/questions/21396279/display-image-and-validation-of-image-extension-before-uploading-file-using-java
    */
}