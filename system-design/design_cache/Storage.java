package design_cache;

public interface Storage {
    public void add(String key, Object value);
    public Object get(String key) throws ItemNotFoundException;
    public void remove(String key) throws ItemNotFoundException;
    public int size();
}
