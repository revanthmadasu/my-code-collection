/**
 * Asked in Swiggy
 * given a sorted array. return a balanced subtree from that sorted array
 */
/**
 * Node{
 *      left: 1, // pointer to node
 *      val: 2 // value
 *      right: 3 // pointer
 * }
 */

 function getBalancedSubtree(array) {
    console.log(`array is ${array}`);
    if (array.length === 0) return null;
    if (array.length <= 3) {
        if (array.length === 1) {
            return {
                value: array[0],
                left: null,
                right: null
            }
        } else if (array.length === 2) {
            const rightNode = {
                value: array[1],
                left: null,
                right: null
            }
            const center = {
                value: array[0],
                left: null,
                right: rightNode
            }
            return center;
        } else {
            const rightNode = {
                value: array[2],
                left: null,
                right: null
            }
            const leftNode = {
                value: array[0],
                left: null,
                right: null
            }
            const center = {
                value: array[1],
                left: leftNode,
                right: rightNode
            }
            return center;
        }
    } else {
        const mid = Math.floor(array.length/2);
        const leftItems = array.slice(0,mid-1);
        const rightItems = array.slice(mid, array.length);
        const leftSubTree = getBalancedSubtree(leftItems);
        const rightSubTree = getBalancedSubtree(rightItems);
        return {
            left: leftSubTree,
            value: array[mid - 1],
            right: rightSubTree
        }
    }
}

function convertToList(node) {
    // let curVal = node.value;
    const array = [];
    let curNode = node;
    while(curNode.next) {
        array.push(curNode.value);
        curNode = curNode.next;
    }
    if (curNode) {
        array.push(curNode.value)
    }
    return array;
}

const node5 = {
    value: 5,
    next: null
}
const node4 = {
    value: 4,
    next: node5
}
const node3 = {
    value: 3,
    next: node4
}
const node2 = {
    value: 2,
    next: node3
}
const node1 = {
    value: 1,
    next: node2
}
const arr = convertToList(node1);
console.log(arr);
const balancedTree = getBalancedSubtree(arr);
console.log(JSON.stringify(balancedTree));