package design_cache;

public class Cache {
    private EvictionPolicy evictionPolicy;
    Cache(EvictionPolicyFactory policyFactory, StorageFactory storageFactory, int maxSize) {
        this.evictionPolicy = policyFactory.getEvictionPolicy(storageFactory, maxSize);
    }
    public void addItem(String key, Object value) {
        this.evictionPolicy.addItem(key, value);
    }
    public Object get(String key) {
        Object value;
        try {
            value = this.evictionPolicy.get(key);
        } catch (ItemNotFoundException exception) {
            return null;
        }
        return value;
    }
}
