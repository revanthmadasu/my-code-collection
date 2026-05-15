/**
 * Problem: https://leetcode.com/problems/shuffle-string
 * Concepts: HashMap
 * 
 */
class Solution {
    public String restoreString(String s, int[] indices) {
        HashMap<Integer, Integer> indicesMap = new HashMap<>();
        for (int i=0; i < indices.length; i++) {
            indicesMap.put(indices[i], i);
        }
        String res = "";
        for (int i=0; i < indices.length; i++) {
            res = res + s.charAt(indicesMap.get(i));
        }
        return res;
    }
}