'''
    problem: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
    concepts: BFS, Binary Tree, Tree
    performance: 45.45% runtime, 8.31% memory
    #todo: improve performance. try without tracking parent, using single bfs or dfs
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pFound = False
        qFound = False
        def dfs(parent, node):
            nonlocal pFound, qFound
            if not node:
                return
            node.parent = parent
            if node == p:
                pFound = True
            if node == q:
                qFound = True
            if pFound and qFound:
                return
            if node.left:
                dfs(node, node.left)
            if node.right:
                dfs(node, node.right)
            return
        dfs(None, root)
        pPath = []
        qPath = []
        pCur = p
        qCur = q
        while pCur:
            pPath.append(pCur)
            pCur = pCur.parent
        while qCur:
            qPath.append(qCur)
            qCur = qCur.parent
        leastCommon = root
        # print(f'pPath: {[p.val for p in pPath]}')
        # print(f'qPath: {[q.val for q in qPath]}')
        while len(pPath) and len(qPath) and pPath[-1] == qPath[-1]:
            leastCommon = pPath[-1]
            pPath.pop()
            qPath.pop()
        return leastCommon