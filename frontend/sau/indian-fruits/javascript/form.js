const formId = 'fruitsSurveyForm';

function validateName(showMessage = false) {
    const formItemElement = document.getElementById("nameInput");
    const name = formItemElement.value;
    const nameRegEx = /^[A-Za-z ,\.]{2,30}$/;
    const isValid = nameRegEx.test(name);
    markIfInvalid(isValid, "nameInput", showMessage, "nameErrorMsg");
    return isValid;
}

function validateFruitName(showMessage = false) {
    const formItemElement = document.getElementById("fruitNameInput");
    const name = formItemElement.value;
    const nameRegEx = /^[A-Za-z ,\.]{2,30}$/;
    const isValid = nameRegEx.test(name);
    markIfInvalid(isValid, "fruitNameInput", showMessage, "fruitNameErrorMsg");
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

function validateTaste(showMessage = false) {
    const selectedTech = document.getElementById(formId).elements['selectTaste'].value;
    const formErrorElement = document.getElementById("tasteErrorMsg");
    const isValid = selectedTech;

    const formElement = document.getElementById("tastesCheckGroup");
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
    return !!isValid;
}

function validateSatisfaction(showMessage = false) {
    const formItemElement = document.getElementById("selectSatisfaction");
    const isValid = formItemElement.value && formItemElement.value !== '0';
    markIfInvalid(isValid, "selectSatisfaction", showMessage, "satisfactionErrorMsg");
    return isValid;
}

function validateFeedback(showMessage = false) {
    const formItemElement = document.getElementById("feedbackInput");
    const isValid = !!(formItemElement.value && formItemElement.value.length >= 15 && formItemElement.value.length <= 250);
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

function validateOnSubmit() {
    const validationResponses = [
        validateName(true),
        validateEmail(true),
        validatePhone(true),
        validateAge(true),
        validateFruitName(true),
        validateTaste(true),
        validateSatisfaction(true),
        validateFeedback(true)
    ];
    if (validationResponses.every(res => res)) {
        // error does not exists
        const formResponses = {
            name: document.getElementById("nameInput").value,
            email: document.getElementById("emailInput").value,
            phone: document.getElementById("phoneInput").value,
            age: Number.parseInt(document.getElementById("ageInput").value),
            primaryTechnology: document.getElementById(formId).elements['selectTaste'].value,
            difficulty: document.getElementById("nameInput").value,
            feedback: document.getElementById("feedbackInput").value
        };
        alert(`Your form is processed with values ${JSON.stringify(formResponses)}`);
    } else {
        alert("Your form has errors. Please check the messages and fill the form again.")
    }
}

function checkIfFruitSelected() {
    const urlParams = new URLSearchParams(window.location.search);
    const fruitName = urlParams.get('fruitName');
    if (fruitName) {
        const formItemElement = document.getElementById("fruitNameInput");
        formItemElement.setAttribute('value', fruitName);
        validateFruitName();
    }
}