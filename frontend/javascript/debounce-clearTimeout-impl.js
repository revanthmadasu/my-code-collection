/**
 * https://leetcode.com/problems/debounce
 * Concepts: Javascript, debounce, timeout, call, apply, polyfills
 * runtime: 63/100, memory: 76/100
 */

function myFunction (id, event) {
    const element = document.getElementById(id);
    console.log(`Search term is ${element.value}`);
}

function samplePrint(index) {
    console.log(`hello ... ${index}`);
}

function getDebounce(fn, delay, ...args) {
    let timeoutId;
    return function(...args) {
        const applyFunc = () => fn.apply({}, args);
        if (timeoutId) {
            clearTimeout(timeoutId);
        }
        timeoutId = setTimeout(applyFunc, delay);
    }
}
const actionDebounce = getDebounce(samplePrint, 1000);
setTimeout(() => console.log(actionDebounce(0)), 1200);
for (let i = 1; i < 10; ++i) {
    actionDebounce(i);
}
// const actionThrottle = (event) => {
//     console.log(event);
// }
