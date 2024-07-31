package system_design.design_inventory_management.classes;

import java.util.List;

import system_design.design_inventory_management.exceptions.ItemsNotSufficientException;
import system_design.design_inventory_management.exceptions.LocationNotSupportedException;

import java.util.Collections;
import java.util.ArrayList;
public class Cart {
    private User user;
    private List<OrderItem> orderItems;
    private Inventory inventory;
    Cart(User user) throws LocationNotSupportedException {
        this.user = user;
        this.inventory = Inventory.getInventory(user.getLocation());
        this.orderItems = new ArrayList<>();
    }

    public boolean addItems(Product product, int quantity) throws ItemsNotSufficientException {
        if (this.inventory.checkProductAdd(product, quantity)) {
            OrderItem orderItem = new OrderItem(product, quantity);
            this.orderItems.add(orderItem);
            return true;
        }
        throw new ItemsNotSufficientException(product, quantity);
    }

    public List<OrderItem> getOrderItems() {
        return Collections.unmodifiableList(this.orderItems);
    }

    public Order makeOrder() throws ItemsNotSufficientException{
        return this.inventory.makeOrder(this);
    }
}
