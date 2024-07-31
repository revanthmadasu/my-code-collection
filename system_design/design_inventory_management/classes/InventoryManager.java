package system_design.design_inventory_management.classes;

import system_design.design_inventory_management.exceptions.ItemsNotSufficientException;
import system_design.design_inventory_management.exceptions.LocationNotSupportedException;

public class InventoryManager {
    private String userName;
    public InventoryManager(String userName) {
        this.userName = userName;
    }
    public Inventory getInventory(String location) throws LocationNotSupportedException {
        return Inventory.getInventory(location);
    }
    public Inventory createInventory(String location) throws LocationNotSupportedException {
        return Inventory.createInventory(location);
    }
    public void addItems(Product product, int quantity, String location) throws LocationNotSupportedException {
        this.getInventory(location).addItems(product, quantity);
    }
    public void removeItems(Product product, int quantity, String location) throws ItemsNotSufficientException, LocationNotSupportedException {
        this.getInventory(location).removeItems(product, quantity);
    }

    public Product createProduct(String productId) {
        return new Product(productId);
    }
}
