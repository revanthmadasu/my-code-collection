/*
    problem: https://leetcode.com/problems/kth-largest-element-in-a-stream
    concepts: Heaps, MinHeap
    performance: 9.9% runtime, 76.31% memory
*/
import java.util.PriorityQueue;
class KthLargest {
    PriorityQueue<Integer> minHeap;
    int capacity;
    public KthLargest(int k, int[] nums) {
        this.minHeap = new PriorityQueue<Integer>();
        this.capacity = k;
        for(int num: nums) {
            this.minHeap.add(num);
        }
        for (int i = 0; i < nums.length - (k); ++i) {
            this.minHeap.poll();
        }
    }
    
    public int add(int val) {
        // System.out.println(String.format("for val: %d - %s", val, this.minHeap.toString()));
        this.minHeap.add(val);
        if (this.minHeap.size() > this.capacity) {
            this.minHeap.poll();
        }
        return this.minHeap.peek();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */