package design_cache;

public interface EvictionPolicyFactory {
    public EvictionPolicy getEvictionPolicy(StorageFactory storageFactory, int maxSize);
}
