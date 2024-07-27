package design_pub_sub;

public class SocialMediaSubscriber implements Subscriber {
    public String name;
    SocialMediaSubscriber(String name) {
        this.name = name;
    }
    @Override
    public void receiveMessage(Message message) {
        System.out.println(String.format("message received by %s - message: %s", this.name, message.getMessage(this)));
    }
}
