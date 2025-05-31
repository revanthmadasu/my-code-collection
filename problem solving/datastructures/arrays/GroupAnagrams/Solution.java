/*
    problem: https://leetcode.com/problems/group-anagrams/
    concepts: Arrays, Sorting
    performance: 99.78% runtime, 90.82% memory
*/
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> anagramsMap = new HashMap();
        List<List<String>> result = new LinkedList();
        for (String str: strs) {
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            String sortedStr = new String(chars);
            if (anagramsMap.containsKey(sortedStr)) {
                anagramsMap.get(sortedStr).add(str);
            } else {
                List<String> anagramsList= new LinkedList();
                anagramsList.add(str);
                anagramsMap.put(sortedStr, anagramsList);
                result.add(anagramsList);
            }
        }
        return result;
    }
}