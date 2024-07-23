import java.util.LinkedList;
import java.util.HashMap;
class LFUCache {
    class Node {
        int key, value, frequency;
        Node(int key, int value) {
            this.key = key;
            this.value = value;
            this.frequency = 0;
        }
    }
    HashMap <Integer, LinkedList<Node>> frequenciesMap;
    HashMap <Integer, Node> nodesMap;
    int capacity, leastFrequency;
    public LFUCache(int capacity) {
        this.capacity = capacity;
        // this.storage = new HashMap<Integer, DequeNode>();
        this.leastFrequency = 1;
        this.nodesMap = new HashMap<Integer, Node>();
        this.frequenciesMap = new HashMap<Integer, LinkedList<Node>>();
    }

    
    public int get(int key) {
        // System.out.println("called get - "+key);
        if (this.nodesMap.containsKey(key)) {
            this.onKeyUsed(key, false);
            return this.nodesMap.get(key).value;
        } else {
            return -1;
        }
    }
    
    public void put(int key, int value) {
        // System.out.println("called put - Key: "+key+ "; Val: "+ value);
        boolean isNew = false;
        if (!this.nodesMap.containsKey(key)) {
            if (this.nodesMap.size() == capacity) {
                Node removingItem = this.frequenciesMap.get(this.leastFrequency).removeLast();
                if (this.frequenciesMap.get(this.leastFrequency).size() == 0) {
                    this.frequenciesMap.remove(this.leastFrequency);
                }
                this.nodesMap.remove(removingItem.key);
            }
            // this.leastFrequency = 1;
            Node node = new Node(key, value);
            this.nodesMap.put(key, node);
            isNew = true;
        } else {
            this.nodesMap.get(key).value = value;
        }
        this.onKeyUsed(key, isNew);
    }

    private void onKeyUsed(int key, boolean isNew) {
        Node curNode = this.nodesMap.get(key);
        curNode.frequency += 1;
        // this.leastFrequency = Math.min(this.leastFrequency, curNode.frequency);
        if (!isNew) {
            // System.out.println("Key:" + curNode.key + " " + calledFrom + " cur freq: " + curNode.frequency);
            this.frequenciesMap.get(curNode.frequency-1).remove(curNode);
        }
        if (!this.frequenciesMap.containsKey(curNode.frequency)) {
            // System.out.println("adding new frequency "+curNode.frequency);
            this.frequenciesMap.put(curNode.frequency, new LinkedList<Node>());
        }
        // System.out.println("adding key "+curNode.key + " to frequency "+curNode.frequency);
        if (isNew) {
            this.leastFrequency = 1;
        } else {
            if (curNode.frequency-1 == this.leastFrequency) {
                if (this.frequenciesMap.get(this.leastFrequency).size()==0) {
                    this.frequenciesMap.remove(this.leastFrequency);
                    this.leastFrequency = curNode.frequency;
                }
            }
        }
        this.frequenciesMap.get(curNode.frequency).addFirst(curNode);
        // System.out.println("Least freq is " + this.leastFrequency);
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */