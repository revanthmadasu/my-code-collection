package design_cache;

public class HashmapStorageFactory implements StorageFactory {

    @Override
    public Storage getStorage() {
        return new HashMapStorage();
    }
    
}
