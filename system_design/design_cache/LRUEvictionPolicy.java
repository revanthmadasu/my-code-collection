package design_cache;
import java.util.LinkedList;
public class LRUEvictionPolicy extends EvictionPolicy {
    private LinkedList<String> keysOrderList;
    LRUEvictionPolicy(StorageFactory storageFactory, int maxSize) {
        super(storageFactory, maxSize);
        //TODO Auto-generated constructor stub
        this.keysOrderList = new LinkedList<String>();
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

    @Override
    protected String getLeastPriorityItem() {
        return this.keysOrderList.pollLast();
    }

    protected void remove(String key) {
        super.remove(key);
        int index = this.keysOrderList.indexOf(key);
        if (index != -1) {
            this.keysOrderList.remove(index);
        }
    }

    private void updateOrder(String key) {
        int index = this.keysOrderList.indexOf(key);
        if (index != -1) {
            this.keysOrderList.remove(index);
        }
        this.keysOrderList.addFirst(key);
    }

    
}
