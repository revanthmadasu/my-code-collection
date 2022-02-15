function myFunction (id, event) {
    const element = document.getElementById(id);
    console.log(`Search term is ${element.value}`);
}

function getThrottle(fn, delay, ...args) {
    var paused = false;
    // console.log(`Args are ${args}`);
    return function (...args) {
        // console.log(`Id is ${id}, event is ${event}`);
        const apply = () => fn.apply({}, args);
        if (!paused) {
            // fn.apply({},args);
            apply();
        }
        // console.log('Setting pasued to true');
        paused = true;
        setTimeout(() => {
            if (paused) {
                // console.log('Paused true is settimeout');
                paused = false;
                // console.log('Set pasued to false in settimeout and calling apply');
                apply();
            }
        }, delay);
    }
}
const actionThrottle = getThrottle(myFunction, 1000)
// const actionThrottle = (event) => {
//     console.log(event);
// }
