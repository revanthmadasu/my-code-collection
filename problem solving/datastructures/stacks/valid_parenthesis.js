/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const stack = [];
    for(let char of s){
        if (char == '(') {
            stack.push('(');
        } else if (char == ')') {
            if (stack[stack.length - 1] == '(') {
                stack.pop();
            } else {
                return false;
            }
        } else if (char == '{') {
            stack.push('{');
        } else if (char == '}') {
            if (stack[stack.length - 1] == '{') {
                stack.pop();
            } else {
                return false;
            }
        } else if (char == '[') {
            stack.push('[');
        } else if (char == ']') {
            if (stack[stack.length - 1] == '[') {
                stack.pop();
            } else {
                return false;
            }
        } 

    }
    return stack.length == 0;
}