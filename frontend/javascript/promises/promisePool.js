/**
 * https://leetcode.com/problems/promise-pool/
 * Concepts: Javascript, Promises, promise callbacks
 * runtime: 31/100, memory: 60/100
 */

/**
 * @param {Function[]} functions
 * @param {number} n
 * @return {Function}
 */
var promisePool = async function(functions, n) {
    let startedTime = new Date().getTime();
    function getTimeTillNow() {
        console.log(`Time counted ${new Date().getTime() - startedTime}`);
    }
    return new Promise(resolve => {
        let curExecutingIndex = 0;
        let executedFunctions = 0;
        let executingFunctions = 0;
        function onResolve(index) {
            console.log(`Executed func(${index}) after ${getTimeTillNow()}`);
            executedFunctions += 1;
            executingFunctions -= 1;
            if (executedFunctions === functions.length) {
                resolve();
            } else {
                executePendingFunctions();
            }
        }
        function executePendingFunctions() {
            console.log(`Executing functions : [${curExecutingIndex}, ${n-executingFunctions})`);
            if (n - executingFunctions > 0) {
                let nextIndex = curExecutingIndex + n - executingFunctions;
                let funcsToExecute = functions.slice(curExecutingIndex, nextIndex);
                executingFunctions += funcsToExecute.length;
                funcsToExecute.forEach((func, index) => {
                    func().then(() => onResolve(index));
                });
                curExecutingIndex = nextIndex;
            }
        }
        if (functions.length) {
            executePendingFunctions();
        } else {
            resolve();
        }
    });
};


const sleep = (t) => new Promise(res => setTimeout(res, t));
promisePool([() => sleep(500), () => sleep(400)], 1)
    .then(console.log) // After 900ms