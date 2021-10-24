public class BasicUser {
    int userId;
    String userName;
    Address address;
    String phoneNumber;
    List<Order> orders;
    UserType userType;
    List<Order> currentOrders;
    public Order addToCart(Dish dish, int quantity);
    public setAddress(Order order, Address address);
    public Payment initializePayment(Order order);
}

public enum UserType {
    END_USER, RESTAURANT_ADMIN
}
public class CustomerUser extends BasicUser {
}

public class RestaurantUser extends BasicUser {
    List<Restaurant> restaurants;
    public boolean addDish(Dish dish, Restaurant restaurant);
    public removeDish(Dish dish, Restaurant restaurant);
    public addRestaurant(Restaurant restaurant);
}

public class Dish {
    int dishId;
    String dishName;
    Cuisine cuisine;
    List<Restaurant> restaurants;
}

public enum Cuisine {
    CONTINENTAL, BIRYANI, SNACK, DESSERT
}

public class Restaurant {
    int restaurantId;
    Address address;
    String phoneNumber;
    List<RestaurantDish> dishes;
    public boolean addDish(Dish dish, float cost);
    public boolean removeDish(RestaurantDish dish);
    public List<Dish> getDishes(List<RestaurantDish> dishes);
}

public class RestaurantDish {
    Dish dish;
    float cost;
}

public class UserService {
    public BasicUser addUser(String userName, Address address, String phoneNumber);
    public boolean editUser(BasicUser user);
    public boolean deleteUser(BasicUser user);
    public makeOrder(Order order, Address address, BasicUser user);


}

public class RestaurantService {
    public List<Restaurant> getRestaurantsByCity(String cityName);
    public List<Restaurant> getRestaurantsByDish(String dishName);
    public List<Restaurant> getRestaurantsByCity(String cityName);

}

public class FoodService {
    public List<Dish> getDishesByName(String dish);
    public List<Dish> getDishesByRestaurant(String restaurantName);

}

public class Order {
    List<CartItem> cartItems;
    float totalAmount;
    OrderState orderState;
    BasicUser user;
    Address address;
}

public enum OrderState {
    NOT_INITIATED, ADDED_TO_CART, PAYMENT_IN_PROGRESS, PAYMENT_FAILED, PAYMENT_SUCCESS, DELIVERY_IN_PROGRESS, DELIVERED
}

public class CartItem {
    Dish dish;
    int quantity;
    float amount;
}

public class PaymentService {
    public Payment startPayment(Order order);
    public PaymentStatus getStatus(Payment payment)
}

public class Payment {
    int paymentId;
    float paymentAmount;
    PaymentStatus status;
}

public enum PaymentStatus {
    PAYMENT_IN_PROGRESS, PAYMENT_FAILED, PAYMENT_SUCCESS
}