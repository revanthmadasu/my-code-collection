/**
 * Problem: https://leetcode.com/problems/differences-between-two-objects/
 * Concepts: Recursion, Backtracking
 * Performance: 87.01% runtime, 32.49% memory
 */
/**
 * @param {Object|Array} obj1
 * @param {Object|Array} obj2
 * @return {Object|Array}
 */
function objDiff(obj1, obj2) {
    let isObj1Ary = obj1 instanceof Array;
    let isObj2Ary = obj2 instanceof Array;
    // console.log(`received : ${JSON.stringify(obj1)}, ${JSON.stringify(obj2)}`);
    if (isObj1Ary ^ isObj2Ary) {
        return [obj1, obj2];
    }
    let diffObj = {};
    for(let key in obj1) {
        // console.log(`curkey: ${key}`);
        if (key in obj2 && JSON.stringify(obj2[key]) !== JSON.stringify(obj1[key])) {
            //console.log(`inequal cond`);
            // if ((obj2[key] instanceof Object && !obj2[key] instanceof Array) && (obj1[key] instanceof Object && !obj1[key] instanceof Array)) {
            if ((obj2[key] instanceof Object) && (obj1[key] instanceof Object)) {
                //console.log(`object inequality cond`);

                let curKeyDiff = objDiff(obj1[key], obj2[key]);
                if (Object.keys(curKeyDiff).length) {
                    diffObj[key] = curKeyDiff;
                }
            } else {
                //console.log(`value inequality cond`);

                diffObj[key] = [obj1[key], obj2[key]];
            }
        } else {
            //console.log(`equal - ${obj1[key]} ${obj2[key]}`);
        }
    }
    if (isObj1Ary && isObj2Ary && JSON.stringify(diffObj) == JSON.stringify({})) {
        return [];
    }
    return diffObj;
};