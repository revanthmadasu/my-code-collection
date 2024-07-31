package system_design.design_inventory_management.classes;

public class Product {
    private String productId;
    Product(String id) {
        this.productId = id;
    }
    public String getProductId() {
        return this.productId;
    }
}
