package design_pub_sub;

public class Publisher {
    private Topic topic;
    Publisher(Topic topic) {
        this.topic = topic;
    }
    public void sendMessage(Message m) {
        this.topic.sendMessage(m);
    }
}
