package system_design.design_inventory_management.classes;

public class Order {
    private Cart cart;
    Order(Cart cart) {
        this.cart = cart;
    }
}
