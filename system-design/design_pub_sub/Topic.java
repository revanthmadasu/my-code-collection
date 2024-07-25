package design_pub_sub;

import java.util.HashSet;

public class Topic {
    private HashSet<Subscriber> subscribers;
    private String topicName;
    Topic(String name) {
        this.topicName = name;
        this.subscribers = new HashSet<>();
    }
    public String getTopicName() {
        return this.topicName;
    }
    public void subscribe(Subscriber sub) {
        this.subscribers.add(sub);
    }
    public void unsubscribe(Subscriber sub) {
        this.subscribers.remove(sub);
    }
    public void sendMessage(Message m) {
        for(Subscriber sub: subscribers) {
            sub.receiveMessage(m);
        }
    }
}
