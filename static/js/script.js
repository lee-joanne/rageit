let signUpMessage = document.getElementById("signup-message");
let signUpHover = document.getElementById("signup-hover");
let postImage = document.getElementById("post_image");

signUpHover.addEventListener("mouseover", showMessage);
signUpHover.addEventListener("mouseout", hideMessage);
postImage.addEventListener("change", imageValidation);

function showMessage() {
    /*
    Function to preview sign up message in Sign Up html page when user hovers mouse over arrow
    */
    signUpMessage.classList.remove("hide");
}

function hideMessage() {
    /*
    Function to hide sign up message in Sign Up html page when user removes mouse from arrow
    */
    signUpMessage.classList.add("hide");
}

function imageValidation() {
    /*
    Function to ensure images match jpeg, jpg, or png before submission.
    Code is taken from Damian Jacob: https://github.com/Damianjacob/MS4_breadit/tree/main/breadit
    */
    let errorMessage = document.getElementById("image-upload-errormessage");

    let fileType = postImage.value;
    let allowedExtensions = ['.jpg', '.jpeg', '.png'];
    let x = 0;
    for (let extension in allowedExtensions) {
        if (fileType.includes(allowedExtensions[extension])) {
            x++;
        } else {}
    }
    if (x < 1) {
        errorMessage.classList.remove("hide");
    }
}