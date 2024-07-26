/*
 * Problem: https://leetcode.com/problems/path-sum-ii/
 * Concepts: Backtracking, Recursion, Tree, LinkedList
 * Performance: 21.88% runtime, 19.54% memory
 */
import java.util.List;
import java.util.LinkedList;
/**
 * Definition for a binary tree node.
 */
class TreeNode {
   int val;
   TreeNode left;
   TreeNode right;
   TreeNode() {}
   TreeNode(int val) { this.val = val; }
   TreeNode(int val, TreeNode left, TreeNode right) {
       this.val = val;
       this.left = left;
       this.right = right;
   }
}
class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        if (root == null) {
            return new LinkedList<>();
        }
        targetSum -= root.val;
        List<List<Integer>> leftNodes = null, rightNodes = null;
        if (root.left == null && root.right == null) {
            if (targetSum == 0) {
                LinkedList<Integer> l = new LinkedList<>();
                l.add(root.val);
                LinkedList<List<Integer>> ll = new LinkedList<>();
                ll.add(l);
                return ll;
            } else {
                return new LinkedList<>();
            }
        }
        if (root.left != null) {
            leftNodes = this.pathSum(root.left, targetSum);
        }
        if (root.right != null) {
            rightNodes = this.pathSum(root.right, targetSum);
        }
        List<List<Integer>> merged = new LinkedList<>();
        if (leftNodes != null && leftNodes.size() > 0) {
            merged.addAll(leftNodes);
        }
        if (rightNodes != null && rightNodes.size() > 0) {
            merged.addAll(rightNodes);
        }
        if (merged.size() > 0) {
            for(List<Integer> arr: merged) {
                arr.addFirst(root.val);
            }
            return merged;
        } else {
            return new LinkedList<>();
        }
    }
}