/**
 * https://leetcode.com/problems/populating-next-right-pointers-in-each-node
 * concepts: queue, bfs
 */

/**
 * // Definition for a Node.
 * function Node(val, left, right, next) {
 *    this.val = val === undefined ? null : val;
 *    this.left = left === undefined ? null : left;
 *    this.right = right === undefined ? null : right;
 *    this.next = next === undefined ? null : next;
 * };
 */

/**
 * @param {Node} root
 * @return {Node}
 */
var connect = function(root) {
    let queue = [root];
    while (queue.length) {
        const newQueue = [];
        for (let i=0; i<queue.length; ++i) {
            const curNode = queue[i];
            if (!curNode) {
                continue;
            }
            if (curNode.left && curNode.right) {
                newQueue.push(curNode.left, curNode.right);
            }
            if (i === queue.length - 1) {
                break;
            }
            curNode.next = queue[i+1];
        }
        queue = newQueue;
    }
    return root;
};