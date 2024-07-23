package design_cache;

import java.util.HashSet;

public abstract class EvictionPolicy {
    private Storage storage;
    int maxSize;
    protected HashSet<String> keys;
    EvictionPolicy(StorageFactory storageFactory, int maxSize) {
        this.storage = storageFactory.getStorage(); 
        this.maxSize = maxSize;
        this.keys = new HashSet<>();
    }
    protected abstract String getLeastPriorityItem();
    public void addItem(String key, Object value) {
        if (!this.canAddItem(key)) {
            String removeKey = this.getLeastPriorityItem();
            this.remove(removeKey);
        }
        this.keys.add(key);
        this.storage.add(key, value);
    }
    public Object get(String key) throws ItemNotFoundException {
        return this.storage.get(key);
    }
    protected void remove(String key) {
        try {
            this.keys.remove(key);
            this.storage.remove(key);
        } catch(Exception e) {
            // log this exception
        }
    }
    private boolean canAddItem(String key) {
        if (this.keys.contains(key)) {
            return true;
        } else {
            return this.keys.size()+1 <= maxSize;
        }
    }
    protected boolean containsKey(String key) {
        return this.containsKey(key);
    }
}
