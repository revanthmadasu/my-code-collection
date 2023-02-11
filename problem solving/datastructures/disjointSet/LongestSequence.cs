/*
    leetcode: https://leetcode.com/problems/longest-consecutive-sequence/description/
    Concepts: DisjointSet, UnionFind
    Memory: 5%, Speed: 5%
    optimization pending
*/
public class Solution {
    class DisjointSet {
        Dictionary<int, HashSet<int>> valuesSetMap;
        public int largestValue = 0;
        public DisjointSet() {
            valuesSetMap = new Dictionary<int, HashSet<int>>();
        }
        public void MakeSet(int value) {
            valuesSetMap[value] = new HashSet<int>();
            valuesSetMap[value].Add(value);
            checkSetLargest(1);
        }
        public HashSet<int> FindSet(int value) {
            return valuesSetMap[value];
        }
        public HashSet<int> Union(int x, int y) {
            // Console.WriteLine("Union is performed on " + x + " and " + y);
            HashSet<int> xSet = valuesSetMap[x];
            HashSet<int> ySet = valuesSetMap[y];
            // Console.WriteLine("Before union: xSet is " + PrintItems(xSet) + " and ySet is " + PrintItems(ySet));

            xSet.UnionWith(ySet);
            // Console.WriteLine("After union: xSet is " + PrintItems(xSet) + " and ySet is " + PrintItems(ySet));
            foreach(int num in ySet) {
                valuesSetMap[num] = xSet;
            }
            // Console.WriteLine("Checking for largest count " + xSet.Count + " and " + this.largestValue);
            checkSetLargest(xSet.Count);
            return xSet;
        }
        public bool ItemExists(int value) {
            return valuesSetMap.ContainsKey(value);
        }
        private void checkSetLargest(int value) {
            largestValue = largestValue > value ? largestValue : value;
            // Console.WriteLine(value + " " + largestValue);
        }
        private String PrintItems(HashSet<int> hashSet) {
            String res = "";
            foreach(int i in hashSet) {
                res += (i + " ");
            }
            return res;
        }
    }
    public int LongestConsecutive(int[] nums) {
        DisjointSet disjointSet = new DisjointSet();
        int largestSequence = 0;
        int[] compareValues = {0,0};
        foreach(int num in nums) {
            if (!disjointSet.ItemExists(num)) {
                disjointSet.MakeSet(num);
            }
            compareValues[0] = num-1;
            compareValues[1] = num+1;
            foreach(int neighVal in compareValues) {
                if (disjointSet.ItemExists(neighVal)) {
                    disjointSet.Union(num, neighVal);
                }
            }
        }
        return disjointSet.largestValue;

    }
}