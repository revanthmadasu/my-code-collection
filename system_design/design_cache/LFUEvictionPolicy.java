package design_cache;
import java.util.HashMap;
import java.util.LinkedList;
public class LFUEvictionPolicy extends EvictionPolicy {
    class Node {
        String key;
        int frequency;
        Node (String key) {
            this.key = key;
            this.frequency = 0;
        }
    }
    private HashMap <String, Node> nodesMap;
    private HashMap <Integer, LinkedList<Node>> frequenciesMap;
    private int leastFrequency = 1;
    LFUEvictionPolicy(StorageFactory storageFactory, int maxSize) {
        super(storageFactory, maxSize);
        this.nodesMap = new HashMap<String, Node>();
        this.frequenciesMap = new HashMap<>();
    }

    public void addItem(String key, Object value) {
        super.addItem(key, value);
        this.updateOrder(key);
    }

    public Object get(String key) throws ItemNotFoundException {
        Object value = super.get(key);
        this.updateOrder(key);
        return value;
    }

    protected String getLeastPriorityItem() {
        String leastPriorityKey =  this.frequenciesMap.get(this.leastFrequency).removeLast().key;
        return leastPriorityKey;
    }

    protected void remove(String key) {
        super.remove(key);
        Node curNode = this.nodesMap.remove(key);
        this.frequenciesMap.get(curNode.frequency).remove(curNode);
        if (this.frequenciesMap.get(curNode.frequency).size() == 0) {
            this.frequenciesMap.remove(curNode.frequency);
        }
        this.leastFrequency = 1;
    }

    private void updateOrder(String key) {
        if (!this.nodesMap.containsKey(key)) {
            this.leastFrequency = 1;
            Node newNode = new Node(key);
            this.nodesMap.put(key, newNode);
        } else {
        }
        Node curNode = this.nodesMap.get(key);

        if (curNode.frequency != 0) {
            this.frequenciesMap.get(curNode.frequency).remove(curNode);
            if (this.frequenciesMap.get(curNode.frequency).size() == 0) {
                this.frequenciesMap.remove(curNode.frequency);
            }
        }
        curNode.frequency += 1;
        if (! this.frequenciesMap.containsKey(curNode.frequency)) {
            this.frequenciesMap.put(curNode.frequency, new LinkedList<Node>());
        }
        this.frequenciesMap.get(curNode.frequency).addFirst(curNode);
    }
}
