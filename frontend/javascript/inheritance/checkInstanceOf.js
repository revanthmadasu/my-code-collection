/**
 * https://leetcode.com/problems/check-if-object-instance-of-class/description/
 * Concepts: Javascript, Inheritance, Prototype Chaining, __proto__, prototype
 * Runtime: 5.31/100, Memory: 6.38/100
 */

/**
 * @param {any} obj
 * @param {any} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    if (obj == null || obj == undefined || classFunction == null || classFunction == undefined) {
        return false;
    } else if (classFunction == Object) {
        return true;
    }
    if (typeof obj == 'number') {
        if (classFunction == Number) {
            return true;
        }
    } else if (typeof obj == 'boolean') {
        if (classFunction == Boolean) {
            return true;
        }
    } else if (typeof obj == 'string') {
        if (classFunction == String) {
            return true;
        }
    }
    let objProto = obj;
    let isInstance = false;
    while (objProto) {
        if (objProto === classFunction.prototype) {
            isInstance = true;
            break;
        }
        objProto = objProto.__proto__;
    }
    return isInstance;
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */