package design_cache;

public class LRUEvictionPolicyFactory implements EvictionPolicyFactory {

    @Override
    public EvictionPolicy getEvictionPolicy(StorageFactory storageFactory, int maxSize) {
        return new LRUEvictionPolicy(storageFactory, maxSize);
    }
    
}
