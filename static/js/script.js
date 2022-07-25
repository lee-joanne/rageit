let signUpMessage = document.getElementById("signup-message");
let signUpHover = document.getElementById("signup-hover");

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

function imageValidation() {
    /*
    Function to ensure images match jpeg, jpg, or png before submission.
    Inspired by code from https://stackoverflow.com/questions/21396279/display-image-and-validation-of-image-extension-before-uploading-file-using-java
    as well as https://github.com/Damianjacob/MS4_breadit/tree/main/breadit
    */
    let postImage = document.getElementById("post_image");
    let errorMessage = document.getElementById("image-upload-errormessage");

    let fileType = postImage.value;
    let allowedExtensions = ['.jpg', '.jpeg', '.png'];
    x = 0;
    for (let extension in allowedExtensions) {
        if (fileType.includes(allowedExtensions[extension])) {
            x++;
        } else {}
    }
    if (x < 1) {
        errorMessage.classList.remove("hide");
    }
}