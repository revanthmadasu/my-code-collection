package system_design.design_inventory_management.classes;
import java.util.ArrayList;
import system_design.design_inventory_management.exceptions.*;;
public class User {
    private String username;
    private ArrayList<Order> orders;
    private Cart cart;
    private String location;
    public User(String username, String location) throws LocationNotSupportedException {
        this.username = username;
        this.orders = new ArrayList<>();
        this.location = location;
        this.cart = new Cart(this);
    }
    public boolean addItem(Product product, int quantity) throws ItemsNotSufficientException {
        return this.cart.addItems(product, quantity);
    }
    public String getLocation() {
        return this.location;
    }
    public Order makeOrder() throws ItemsNotSufficientException{
        return this.cart.makeOrder();
    }
}
