package design_stack_overflow;

import java.util.ArrayList;

public class Answer implements Post {
    String answer;
    int upVoteCount, downVoteCount;
    private User user;
    private ArrayList<Comment> comments;
    Answer(String answer, User user) {
        this.answer = answer;
        this.upVoteCount = 0;
        this.downVoteCount = 0;
        this.comments = new ArrayList<>();
        this.user = user;
    }
    @Override
    public void upVote() {
        this.upVoteCount += 1;
    }

    @Override
    public void downVote() {
        this.downVoteCount += 1;
    }

    @Override
    public void comment(String comment, User user) {
        this.comments.add(new Comment(this, comment, user));
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(String.format("Answer by %s: \n\t %s \n", this.user.username, this.answer));
        sb.append("\t Comments:\n");
        for (Comment comment: comments) {
            sb.append(String.format("\t\t%s", comment));
        }
        return sb.toString();
    }    
}
