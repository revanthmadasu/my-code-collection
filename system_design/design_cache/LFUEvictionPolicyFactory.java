package design_cache;

public class LFUEvictionPolicyFactory implements EvictionPolicyFactory {

    @Override
    public EvictionPolicy getEvictionPolicy(StorageFactory storageFactory, int maxSize) {
        return new LFUEvictionPolicy(storageFactory, maxSize);
    }
    
}
