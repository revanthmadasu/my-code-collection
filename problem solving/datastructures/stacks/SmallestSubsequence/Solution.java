/*
    problem: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
    concepts: stack, monotonic stack, streams
    performance: 26.16% runtime, 41.45% memory
*/
/*
cbacdcbc
01234567

acdb
*/
import java.util.LinkedList;
import java.util.HashMap;
import java.util.HashSet;
// import java.util.stream.Collectors;
class Solution {
    public String smallestSubsequence(String s) {
        HashMap<Character, Integer> occurancesMap = new HashMap<>();
        for (int i = 0; i < s.length(); ++i) {
            char ch = s.charAt(i);
            occurancesMap.put(ch, i);
        }
        LinkedList<Character> stack = new LinkedList<>();
        HashSet<Character> visited = new HashSet<>();
        for (int i = 0; i < s.length(); ++i) {
            Character ch = s.charAt(i);
            if (!visited.contains(ch)) {
                if (!(stack.size() == 0 || stack.getLast() < ch || occurancesMap.get(stack.getLast()) < i)) {
                    while (stack.size() > 0 && stack.getLast() > ch && occurancesMap.get(stack.getLast()) > i) {
                        Character rmCh = stack.removeLast();
                        visited.remove(rmCh);
                    }
                }
                stack.addLast(ch);
                visited.add(ch);
            }
        }
        String res = "";
        for (Character ch: stack) {
            res += ch.toString();
        }
        return res;
        // return stack.stream().map(String::valueOf).collect(Collectors.joining());
    }
}