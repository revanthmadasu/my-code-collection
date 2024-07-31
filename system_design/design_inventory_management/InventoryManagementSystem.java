package system_design.design_inventory_management;

import system_design.design_inventory_management.classes.InventoryManager;
import system_design.design_inventory_management.classes.Product;
import system_design.design_inventory_management.classes.User;
import system_design.design_inventory_management.exceptions.ItemsNotSufficientException;
import system_design.design_inventory_management.exceptions.LocationNotSupportedException;

public class InventoryManagementSystem {
    public static void main(String args[]) {
        try {
            InventoryManager manager = new InventoryManager("jack");
            manager.createInventory("hyderabad");
            manager.createInventory("dallas");
            Product macLaptop = manager.createProduct("macbook");
            Product dellLaptop = manager.createProduct("dell inspirion");
            manager.addItems(macLaptop, 5, "hyderabad");
            manager.addItems(macLaptop, 15, "dallas");
            manager.addItems(dellLaptop, 25, "hyderabad");
            manager.addItems(dellLaptop, 10, "dallas");
            User user1 = new User("John", "dallas");
            User user2 = new User("Naresh", "hyderabad");

            user1.addItem(dellLaptop, 5);
            user2.addItem(dellLaptop, 10);
            user1.makeOrder();
            user2.makeOrder();
            User user3 = new User("John", "dallas"); 
            user3.addItem(dellLaptop, 5);
            System.out.println("Successful");

        } catch (ItemsNotSufficientException e) {
            System.out.println(e.getMessage());
        } catch (LocationNotSupportedException e) {
            System.out.println(e.getMessage());
        }

    }
}
