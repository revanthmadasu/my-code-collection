'''
    Problem: https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries
    Concepts: Tree, Binary Tree, DFS, BFS, Heaps
    performance: 29.40% runtime, 21.79% memory
'''
import heapq
from typing import Optional
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        nodesDict = dict()

        def dfs(node, parent):
            nodesDict[node.val] = node
            node.parent = parent
            leftHeight, rightHeight = -1, -1
            if node.left:
                leftHeight = dfs(node.left, node)
            if node.right:
                rightHeight = dfs(node.right, node)
            node.height = max(leftHeight, rightHeight) + 1
            return node.height

        dfs(root, None)

        def updateParentHeights(parent):
            leftHeight = parent.left.height if parent.left else -1
            rightHeight = parent.right.height if parent.right else -1
            parent.height = max(leftHeight, rightHeight) + 1
            if parent.parent:
                updateParentHeights(parent.parent)
        precomp = dict()
        q = [root]
        while q:
            newQ = []
            maxHeap = [-node.height for node in q]
            heapq.heapify(maxHeap)
            for node in q:
                height = heapq.heappop(maxHeap)
                if height != -(node.height):
                    precomp[node.val] = root.height
                elif maxHeap:
                    diff = -(height - maxHeap[0])
                    precomp[node.val] = root.height - diff
                else:
                    # print(f'removing {node.val}')
                    precomp[node.val] = root.height + (height-1)
                if node.left:
                    newQ.append(node.left)
                if node.right:
                    newQ.append(node.right)
                heapq.heappush(maxHeap, height)
            q = newQ
        ans = []
        for query in queries:
            ans.append(precomp[query])
            # height = nodesDict[query].height
            # nodesDict[query].height = -1
            # updateParentHeights(nodesDict[query].parent)
            # ans.append(root.height)
            # nodesDict[query].height = height
            # updateParentHeights(nodesDict[query].parent)
        return ans
