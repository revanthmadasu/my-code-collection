/**
 * https://leetcode.com/problems/curry
 * concepts: currying, closure, recursion, function arguments
 * runtime: 81/100, memory: 94/100
 */
/**
 * @param {Function} fn
 * @return {Function}
 */
var curry = function(fn) {
    function getArguments(func) {
        // Convert the function to a string
        const funcString = func.toString();

        // Use a regular expression to extract the arguments
        const argsMatch = funcString.match(/\((.*?)\)/);

        if (argsMatch && argsMatch[1]) {
            // Split the matched arguments by commas
            const args = argsMatch[1].split(',');

            // Trim whitespace from each argument
            const trimmedArgs = args.map((arg) => arg.trim());

            return trimmedArgs;
        }
    }
    const defArgs = getArguments(fn) || [];
    const receivedArgs = [];
    return function curried(...args) {
        receivedArgs.push(...args);
        console.log(`Current Received Args: ${args} \t All Received Args ${receivedArgs}`);
        if (receivedArgs.length >= defArgs.length) {
            return fn(...receivedArgs);
        } else {
            return curried;
        }
    };
};


function sum(a, b) { return a + b; }
const csum = curry(sum);
console.log(csum(1)(2)) // 3
 