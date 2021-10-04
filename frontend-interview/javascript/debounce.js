function myFunction (id, event) {
    const element = document.getElementById(id);
    console.log(`Search term is ${element.value}`);
}

function getDebounce(fn, delay, ...args) {
    var paused = 0;
    // console.log(`Args are ${args}`);
    return function (...args) {
        // console.log(`Id is ${id}, event is ${event}`);
        const apply = () => fn.apply({}, args);
        // console.log('Setting pasued to true');
        ++paused;
        setTimeout(() => {
            --paused;
            if (!paused) {
                apply();
            }
        }, delay);
    }
}
const actionDebounce = getDebounce(myFunction, 1000)
// const actionThrottle = (event) => {
//     console.log(event);
// }
