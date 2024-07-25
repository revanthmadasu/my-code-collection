package design_pub_sub;

public class Message {
    private Object message;
    public Message(Object message) {
        this.message = message;
    }
    public Object getMessage(Subscriber sub) {
        return this.message;
    }
}
