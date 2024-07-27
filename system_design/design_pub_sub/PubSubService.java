package design_pub_sub;
import java.util.HashMap;
public class PubSubService {
    private static PubSubService pubSubService;
    public static PubSubService getPubSubService() {
        if (PubSubService.pubSubService == null) {
            PubSubService.pubSubService = new PubSubService();
        }
        return PubSubService.pubSubService;
    }
    private HashMap<String, Topic> topicsMap;
    private PubSubService() {
        this.topicsMap = new HashMap<>();
    }
    public Topic getTopic(String topic) throws TopicNotFoundException {
        if (!this.topicsMap.containsKey(topic)) {
            throw new TopicNotFoundException();
        }
        return this.topicsMap.get(topic);
    }
    public Topic createTopic(String topic) throws TopicAlreadyExists {
        if (this.topicsMap.containsKey(topic)) {
            throw new TopicAlreadyExists();
        }
        this.topicsMap.put(topic, new Topic(topic));
        return this.topicsMap.get(topic);
    }
    public Publisher getPublisher(String topic) throws TopicNotFoundException {
        return new Publisher(this.getTopic(topic));
    }
    public void sendMessage(Message message, String topicStr) throws TopicNotFoundException {
        Topic topic = this.getTopic(topicStr);
        this.sendMessage(message, topic);
    }
    public void sendMessage(Message message, Topic topic) throws TopicNotFoundException {
        topic.sendMessage(message);
    }
}
