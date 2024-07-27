package design_stack_overflow;

public class Stackoverflow {
    public static void main(String args[]) {
        try {
            User user1 = User.register("revanth", "m_pword");
            User user2 = User.register("Swapna", "s_pword");
            Question q1 = user1.postQuestion("Hello peeps. how are you?");
            Answer ans = user2.answerQuestion(q1, "I'm good Revanth. how are you?");
            user1.comment(ans, "I'm doing good too Swapna");
            User user3 = User.register("Ravi", "r_pword");
            System.out.println(user3.viewQuestion(q1.id));
            user3.comment(q1, "guys.. this app is not for meet and greet.");
            System.out.println(user3.viewQuestion(q1.id));

        } catch (Exception e) {
            System.err.println(String.format("Exception occured at %s", e.toString()));
            System.out.println(e.getMessage());
        }
    }
}
