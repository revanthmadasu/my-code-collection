package system_design.design_inventory_management.classes;

public class OrderItem {
    private Product product;
    private int quantity;
    OrderItem(Product product, int quantity) {
        this.product = product;
        this.quantity = quantity;
    }
    public Product getProduct() {
        return this.product;
    }
    public int getQuantity() {
        return this.quantity;
    }
}
