var cloneGraph = function(node) {
    let nodeMap = new Map(), clonedNodes = [];
    let queue = [node];
    while (queue.length) {
        let curNode = queue.splice(0,1)[0];
        if (!curNode) continue;
        if (!nodeMap.has(curNode)) {
            // console.log('Node not there in map');
            const clonedNode = {val: curNode.val, neighbors: []};
            clonedNodes.push(clonedNode);
            if (curNode.neighbors && curNode.neighbors.length) {
                // console.log('pushing nodes');
                queue.push(...curNode.neighbors);
            }
            nodeMap.set(curNode, clonedNode);
        }
    }
    // console.log('Nodes in nodemap are ',nodeMap.keys());
    for(let curNode of nodeMap.keys()) {
        // console.log('cur node is ', JSON.stringify(curNode));
        let clonedNode = nodeMap.get(curNode);
        clonedNode.neighbors = curNode.neighbors.map(nd => nodeMap.get(nd));
    }
    return nodeMap.get(node);
};
 
let a = {
    val: 1,
    neighbors: []
};
 
let b = {
    val: 2,
    neighbors: []
}
 
let c = {
    val: 3,
    neighbors: []
};
 
let d = {
    val: 4,
    neighbors: []
}
a.neighbors = [b,d];
b.neighbors = [a,c];
d.neighbors = [a,c];
c.neighbors = [b,d];
 
let clonedNode = cloneGraph(a);
// console.log('CLoned obj is \n', JSON.stringify(clonedNode));
a.neighbors[0].neighbors[1].val = 100;
console.log(clonedNode.neighbors[0].neighbors[1].val);
 

