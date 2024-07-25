package design_pub_sub;

public interface Subscriber {
    public void receiveMessage(Message message);
}
