'''
    Problem: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
    Concepts: BFS, Trees, Queue, Design
    performance: 97.96% runtime, 91.37% memory
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        '''
        outputs: "1,2,3,na,na,4,5,na,na,na,na"
        '''
        nodes = []
        q = deque()
        q.append(root)
        while len(q):
            node = q.popleft()
            if node:
                nodes.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                nodes.append("na")
        nodes = ",".join(nodes)
        # print(f'sent: {nodes}')
        return nodes

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        '''
        receives: "1,2,3,na,na,4,5,na,na,na,na"
        '''
        nodes = data.split(",")
        if nodes[0] == "na":
            return None
        # print(f'received: {nodes}')
        root = TreeNode(int(nodes[0]))
        q = deque()
        q.append(root)
        i = 1
        while len(q):
            node = q.popleft()
            if nodes[i] != "na":
                newNode = TreeNode(int(nodes[i]))
                node.left = newNode
                q.append(newNode)
            if nodes[i+1] != "na":
                newNode = TreeNode(int(nodes[i+1]))
                node.right = newNode
                q.append(newNode)
            i += 2
        return root
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))