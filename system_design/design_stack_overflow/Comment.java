package design_stack_overflow;

public class Comment {
    Post post;
    String comment;
    private User user;
    Comment(Post post, String comment, User user) {
        this.post = post;
        this.comment = comment;
        this.user = user;
    }
    public String toString() {
        return String.format("Comment by %s: %s", user.username, comment);
    }
}
