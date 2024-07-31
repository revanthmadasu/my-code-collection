package system_design.design_inventory_management.classes;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import system_design.design_inventory_management.exceptions.ItemsNotSufficientException;
import system_design.design_inventory_management.exceptions.LocationNotSupportedException;

public class Inventory {
    private HashMap<String, Integer> productCounts;
    private static HashMap<String, Inventory> inventoryMap = new HashMap<>();
    private Inventory() {
        this.productCounts = new HashMap<>();
    }
    static Inventory createInventory(String location) {
        if (!Inventory.inventoryMap.containsKey(location)) {
            Inventory.inventoryMap.put(location, new Inventory());
        }
        return Inventory.inventoryMap.get(location);
    }
    public static Inventory getInventory(String location) throws LocationNotSupportedException {
        if (!Inventory.inventoryMap.containsKey(location)) {
            throw new LocationNotSupportedException(location);
        }
        return Inventory.inventoryMap.get(location);
    }
    public void addItems(Product product, int quantity) {
        String pId = product.getProductId();
        if (!this.productCounts.containsKey(pId)) {
            this.productCounts.put(pId, 0);
        }
        this.productCounts.put(pId, this.productCounts.get(pId) + quantity);
    }

    public void removeItems(Product product, int quantity) throws ItemsNotSufficientException {
        if (!this.checkProductAdd(product, quantity)) {
            throw new ItemsNotSufficientException(product, quantity);
        }
        this.productCounts.put(product.getProductId(), this.productCounts.get(product.getProductId()) - quantity);
    }

    public boolean checkProductAdd(Product product, int quantity) {
        String pId = product.getProductId();
        return this.productCounts.containsKey(pId) && this.productCounts.get(pId) >= quantity;
    }

    public Order makeOrder(Cart cart) throws ItemsNotSufficientException{
        List<OrderItem> orderItems = cart.getOrderItems();
        List<OrderItem> processed = new ArrayList<>();
        for (OrderItem orderItem: orderItems) {
            try {
                this.removeItems(orderItem.getProduct(), orderItem.getQuantity());
                processed.add(orderItem);
            } catch (ItemsNotSufficientException e) {
                this.addItems(processed);
                throw new ItemsNotSufficientException(orderItem.getProduct(), orderItem.getQuantity());
            }
        }
        Order order = new Order(cart);
        return order;
    }

    public void addItems(List<OrderItem> orderItems) {
        orderItems.stream().forEach(orderItem -> this.addItems(orderItem.getProduct(), orderItem.getQuantity()));
    }


}
