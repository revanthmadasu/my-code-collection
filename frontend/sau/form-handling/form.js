const formId = 'techSurveyForm';

function validateName(showMessage = false) {
    const formItemElement = document.getElementById("nameInput");
    const name = formItemElement.value;
    const nameRegEx = /^[A-Za-z ,\.]{2,30}$/;
    const isValid = nameRegEx.test(name);
    markIfInvalid(isValid, "nameInput", showMessage, "nameErrorMsg");
    return isValid;
}

function validateEmail(showMessage = false) {
    const formItemElement = document.getElementById("emailInput");
    const email = formItemElement.value;
    const emailRegEx = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    const isValid = emailRegEx.test(email);
    markIfInvalid(isValid, "emailInput", showMessage, "emailErrorMsg");
    return isValid;
}

function validatePhone(showMessage = false) {
    const formItemElement = document.getElementById("phoneInput");
    const phone = formItemElement.value;
    const phoneRegEx = /^\+?[0-9]{1,3}-?[0-9()\-.\s]{8,}$/;
    const isValid = phoneRegEx.test(phone);
    markIfInvalid(isValid, "phoneInput", showMessage, "phoneErrorMsg");
    return isValid;
}

function validateAge(showMessage = false) {
    const formItemElement = document.getElementById("ageInput");
    const age = Number.parseInt(formItemElement.value);

    const isValid = (!isNaN(age)) && (age >= 12 && age <= 100)
    markIfInvalid(isValid, "ageInput", showMessage, "ageErrorMsg");
    return isValid;
}

function validateTech(showMessage = false) {
    const selectedTech = document.getElementById(formId).elements['selectTech'].value;
    const formErrorElement = document.getElementById("techErrorMsg");
    const isValid = selectedTech;

    const formElement = document.getElementById("primaryTechCheckGroup");
    if (formElement) {
        if (isValid) {
            formElement.classList.add("group-is-valid");
            formElement.classList.remove("group-is-invalid");
            formErrorElement.classList.add("d-none");
            formErrorElement.classList.remove("group-invalid-feedback"); 
        } else {
            formElement.classList.add("group-is-invalid");
            formElement.classList.remove("group-is-valid");
            if (showMessage) {
                formErrorElement.classList.add("group-invalid-feedback");
                formErrorElement.classList.remove("d-none");
            }
        }
    }
    return isValid;
}

function validateDifficulty(showMessage = false) {
    const formItemElement = document.getElementById("nameInput");
    const isValid = formItemElement.value && formItemElement.value !== '0';
    markIfInvalid(isValid, "selectRating", showMessage, "difficultyErrorMsg");
    return isValid;
}

function validateFeedback(showMessage = false) {
    const formItemElement = document.getElementById("feedbackInput");
    const isValid = formItemElement.value && formItemElement.value.length >= 15 && formItemElement.value.length <= 250;
    markIfInvalid(isValid, "feedbackInput", showMessage, "feedbackErrorMsg");
    return isValid;
}

function markIfInvalid(isValid, formItemId, showMessage, errorTag) {
    const formElement = document.getElementById(formItemId);
    const formErrorElement = document.getElementById(errorTag);
    if (formElement) {
        if (isValid) {
            formElement.classList.add("is-valid");
            formElement.classList.remove("is-invalid");
            formErrorElement.classList.add("d-none");
            formErrorElement.classList.remove("invalid-feedback");   
        } else {
            formElement.classList.add("is-invalid");
            formElement.classList.remove("is-valid");
            if (showMessage) {
                formErrorElement.classList.add("invalid-feedback");
                formErrorElement.classList.remove("d-none");
            }
        }
    }
}

function onSubmit(event) {
    console.log("Submit clicked");
    validateName();
    validateEmail();
    validatePhone();
    validateAge();
    validateTech();
    validateDifficulty();
    validateFeedback();
    console.log("Form Processing done")
}

function validateOnSubmit() {
    validateName(true);
    validateEmail(true);
    validatePhone(true);
    validateAge(true);
    validateTech(true);
    validateDifficulty(true);
    validateFeedback(true);
}