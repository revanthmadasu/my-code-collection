/*
    problem: https://leetcode.com/problems/design-circular-queue/
    concepts: linkedlist, queue, FIFO
    performance: 100% runtime, 26.78% memory
*/
class MyCircularQueue {
    class LinkedListNode {
        int val;
        LinkedListNode next;
        LinkedListNode prev;
        LinkedListNode(int val) {
            this.val = val;
        }
    }
    int capacity;
    int currentCapacity;
    LinkedListNode root;
    public MyCircularQueue(int k) {
        this.currentCapacity = 0;
        this.capacity = k;
    }
    
    public boolean enQueue(int value) {
        if (this.isFull()) {
            return false;
        }
        if (this.root == null) {
            this.root = new LinkedListNode(value);
            this.connectCircle(this.root, this.root);
        } else {
            LinkedListNode node = new LinkedListNode(value); 
            this.addAtEnd(node);
            this.connectCircle(this.root, node);
        }
        this.currentCapacity += 1;
        return true;
    }
    
    private void addAtEnd(LinkedListNode end) {
        this.root.prev.next = end;
        end.prev = this.root.prev;
    }
    
    private void connectCircle(LinkedListNode start, LinkedListNode end) {
        start.prev = end;
        end.next = start;
    }
    
    public boolean deQueue() {
        if (this.isEmpty()) {
            return false;
        }
        int val = this.root.val;
        if (this.root != this.root.next) {
            LinkedListNode end = this.root.prev;
            this.root = this.root.next;
            this.connectCircle(this.root, end);
        } else {
            this.root = null;
        }
        this.currentCapacity -= 1;
        return true;
    }
    
    public int Front() {
        if (this.isEmpty()) {
            return -1;
        }
        return this.root.val;
    }
    
    public int Rear() {
        if (this.isEmpty()) {
            return -1;
        }
        return this.root.prev.val;
    }
    
    public boolean isEmpty() {
        return this.currentCapacity == 0;
    }
    
    public boolean isFull() {
        return this.capacity == this.currentCapacity;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */