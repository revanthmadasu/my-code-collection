package design_cache;
import java.util.HashMap;
public class HashMapStorage implements Storage {
    HashMap<String, Object> storage;
    HashMapStorage() {
        storage = new HashMap<String, Object>();
    }
    public void add(String key, Object value) {
        this.storage.put(key, value);
    }
    public Object get(String key) throws ItemNotFoundException{
        if (!this.storage.containsKey(key)) {
            throw new ItemNotFoundException(key);
        }
        return this.storage.get(key);
    }
    public void remove(String key) throws ItemNotFoundException {
        if (this.storage.containsKey(key)) {
            this.storage.remove(key);
        } else {
            throw new ItemNotFoundException(key);
        }
    }
    public int size() {
        return this.storage.size();
    }
}