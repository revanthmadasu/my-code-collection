package design_pub_sub;

public class PubSubDemo {



    public static void main(String args[]) {
        PubSubService pubSubService = PubSubService.getPubSubService();
        SocialMediaSubscriber scienceGuy = new SocialMediaSubscriber("Science stuff topics");
        SocialMediaSubscriber astroGuy = new SocialMediaSubscriber("Astrology stuff topics");
        SocialMediaSubscriber newsGuy = new SocialMediaSubscriber("News stuff topics");
        try {
            Topic nuclearExp = pubSubService.createTopic("nuclear-experiments");
            Topic planetsPositions = pubSubService.createTopic("planets-position-changes");
            Topic celebrityPredictions = pubSubService.createTopic("celebrity-astro");
            nuclearExp.subscribe(scienceGuy);
            nuclearExp.subscribe(newsGuy);
            planetsPositions.subscribe(scienceGuy);
            planetsPositions.subscribe(astroGuy);
            celebrityPredictions.subscribe(newsGuy);
            celebrityPredictions.subscribe(astroGuy);

            nuclearExp.sendMessage(new Message("North Korea conducted nuclear explosions"));
            planetsPositions.sendMessage(new Message("Jupiter movement is changed and getting faster"));
            celebrityPredictions.sendMessage(new Message("Donald Trump has a better chance of winning according to astrology"));

        } catch (Exception e) {
            System.out.println(e.getLocalizedMessage());
        }

        
    }
}
