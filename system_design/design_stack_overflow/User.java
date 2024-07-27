package design_stack_overflow;

import java.util.HashMap;
import java.util.ArrayList;

public class User {
    String username;
    private String password;
    private ArrayList<Question> questions;
    static HashMap<String, User> userDB = new HashMap<String, User>();
    static User register(String username, String password) throws UserCannotCreateException {
        if (User.userDB.containsKey(username)) {
            throw new UserCannotCreateException();
        }
        User user = new User(username, password);
        User.userDB.put(username, user);
        return user;
    }
    static User login(String userName, String password) throws InvalidCredentialsException{
        if (User.userDB.containsKey(userName)) {
            if (User.userDB.get(userName).password == password) {
                return User.userDB.get(userName);
            }
        }
        throw new InvalidCredentialsException();
    }
    public User(String username, String password) {
        this.username = username;
        this.password = password;
        this.questions = new ArrayList<>();
    }
    public Question postQuestion(String question) {
        Question q = new Question(question);
        this.questions.add(q);
        return q;
    }
    public Answer answerQuestion(Question q, String answer) {
        return q.answer(answer, this);
    }
    public Question viewQuestion(int questionId) {
        return Question.getQuestion(questionId);
    }
    public void comment(Post post, String comment) {
        post.comment(comment, this);
    } 
}
