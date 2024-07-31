package system_design.design_inventory_management.exceptions;

import system_design.design_inventory_management.classes.Product;

public class ItemsNotSufficientException extends Exception {
    private String message;
    public ItemsNotSufficientException(Product prod, int quantity) {
        this.message = String.format("Product: %s with quantity %d is not available in our inventory.", prod.getProductId(), quantity);
    }
    public String getMessage() {
        return this.message;
    }
}
