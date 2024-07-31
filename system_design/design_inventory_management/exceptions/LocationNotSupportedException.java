package system_design.design_inventory_management.exceptions;

public class LocationNotSupportedException extends Exception{
    private String message;
    public LocationNotSupportedException(String location) {
        this.message = String.format("Location: %s is not yet established.", location);
    }
    public String getMessage() {
        return this.message;
    }
}
