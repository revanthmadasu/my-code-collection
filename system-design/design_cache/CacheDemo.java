package design_cache;

public class CacheDemo {
    public static void main(String args[]) {
        Cache lfuCache = new Cache(new LFUEvictionPolicyFactory(), new HashmapStorageFactory(), 5);
        Cache lruCache = new Cache(new LRUEvictionPolicyFactory(), new HashmapStorageFactory(), 5);

        String[] operations = {"add", "add", "add", "add", "add", "add", "add", "add", "get", "get"};
        String[] params = {"hello:how are you", "hello:howdy", "hello:supp", "bye:farewell adious", "hi:yoo", "namaste: kaise ho aap", "bonjour:fnksn fjd", "bagunnara: telugu", "hello", "bye"};
        for(int i = 0; i < operations.length; ++i) {
            if (operations[i] == "add") {
                String keyvals[] = params[i].split(":");
                System.out.println("Trying to add: "+ keyvals[0]+":"+keyvals[1]);
                lruCache.addItem(keyvals[0], keyvals[1]);
                lfuCache.addItem(keyvals[0], keyvals[1]);
                System.out.println("Added "+keyvals[0]+" successfully");
            } else {
                String key = params[i];
                System.out.println("Trying to retrieve: " + key);
                System.out.println("LRU cache result: " + lruCache.get(key));
                System.out.println("LFU cache result: " + lfuCache.get(key));
            }
        }
    }
}
