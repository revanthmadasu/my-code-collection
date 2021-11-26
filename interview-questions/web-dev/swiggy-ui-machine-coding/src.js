function payAction() {
    console.log('pay action clicked');
 
    const cardNumberTag = document.getElementById('card-number');
    cardNumberTag.innerHTML = document.getElementById('cardNumberInput').value;
 
    const cardNameTag = document.getElementById('card-name');
    cardNameTag.innerHTML = document.getElementById('nameInput').value;
 
    const validTag = document.getElementById('card-exp-date');
    validTag.innerHTML = document.getElementById('cvcInput').value;
}
 
function validateAccountNumber() {
    const element = document.getElementById('cardNumberInput');
    let value = element.value;
    if (!(ev.key >= '0' && ev.key <= '9')) {
        element.value = value.slice(0, value.length -1);
        return;
    }
    if (value.length < 12) {
        // mark as error
    }
}
 
inps = [
    {
        className: '',
        value: '',
        keydown: () => {
 
        }
    },
    {
        className: '',
        value: '',
        keydown: () => {
           
        }
    }
]
 
function checkAccountNumber(ev) {
    const element = document.getElementById('cardNumberInput');
    let value = element.value;
    if (!(ev.key >= '0' && ev.key <= '9')) {
        element.value = value.slice(0, value.length -1);
        return;
    }
    if (element.value.length === 4 || element.value.length === 9 || element.value.length === 14) {
        element.value += ' ';
    }
}
 
function checkName(ev) {
    const element = document.getElementById('cardNumberInput');
    let value = element.value;
    if (!((ev.key >= 'A' && ev.key <= 'Z') || (ev.key >= 'a' && ev.key <= 'z'))) {
        element.value = value.slice(0, value.length -1);
        return;
    }
}
 
function checkDate(ev) {
    const element = document.getElementById('vaidThruInput');
    let value = element.value;
    if (!(ev.key >= '0' && ev.key <= '9')) {
        element.value = value.slice(0, value.length -1);
        return;
    }
    if (value.length == 2 && value.indexOf('/') === -1) {
        element.value = value + '/';
    }
    if (value.length > 5) {
        element.value = value.slice(0,5);
    }
    ev.stopPropagation();
}