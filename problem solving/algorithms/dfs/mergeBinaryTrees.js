/**
 * https://leetcode.com/problems/merge-two-binary-trees
 * Concepts: Binary Trees, DFS
 */

/**
 * Pending - Lot of memory and runtime optimization to do
 * runtime 56.52 percentile
 * memory: 6.35 percentile
 */

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**


 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {TreeNode}
 */
var mergeTrees = function(root1, root2) {
    let trav1 = root1, trav2 = root2, trav1Vals = {}, trav2Vals = {}, trav1Order = [], trav2Order = [];
    dfsTraversal(trav1, trav1Vals, trav1Order, 's');
    dfsTraversal(trav2, trav2Vals, trav2Order, 's');
    let resVals = {}, resNodesMap = {};
    if (!trav1Order.length && !trav2Order.length) {return null}
    // creates nodes for tree1 and merges if same nodes are there in tree 2 - 0(n)
    trav1Order.forEach(path => {
        resVals[path] = trav1Vals[path].val + (() => {
            if (trav2Vals[path]) {
                trav2Vals[path].read = true;
                return trav2Vals[path].val;
            }
            return 0;
        })();
        resNodesMap[path] = getTreeNode(resVals[path], null, null);
        trav1Vals[path].read = true;
    });
    // creates nodes for tree2 that are not there in tree1 - 0(n)
    trav2Order.forEach(path => {
        if (!trav2Vals[path].read) {
            resVals[path] = trav2Vals[path].val;
            resNodesMap[path] = getTreeNode(resVals[path], null, null);
            trav2Vals[path].read = true;
        }
    });
    const allPaths = Object.keys(resNodesMap);
    const connectedMap = {'s': true};
    const connect = (path) => {
        if (connectedMap[path]) {
            return;
        }
        const prevPath = path.slice(0,-1);
        if (!connectedMap[prevPath]) {
            connect(prevPath);
        }
        const currentNode = resNodesMap[path];
        const prevNode = resNodesMap[prevPath];
        const dir = path[path.length - 1];
        if (dir === 'l') {
            prevNode.left = currentNode;
            connectedMap[path] = true;
        } else if (dir === 'r') {
            prevNode.right = currentNode;
            connectedMap[path] = true;
        }
    };
    // connect all nodes - 0(nlogn)
    allPaths.forEach(path => {
        connect(path);
    });
    return resNodesMap['s'];
}

function dfsTraversal(node,traverseValues, travOrder, path) {
    if (node) {
        travOrder.push(path);
        traverseValues[path] = {val: node.val, read: false};
        if (node.left) {
            dfsTraversal(node.left, traverseValues, travOrder, path+'l');
        }
        if (node.right) {
            dfsTraversal(node.right, traverseValues, travOrder, path+'r');
        }
    } 
}

function getTreeNode(val, left, right) {
    return {
        val: (val===undefined ? 0 : val),
        left: (left===undefined ? null : left),
        right: (right===undefined ? null : right)
    };
 }