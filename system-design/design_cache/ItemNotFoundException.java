package design_cache;

public class ItemNotFoundException extends Exception {
    ItemNotFoundException(String key) {
        super(key + "not found");
    }
}
