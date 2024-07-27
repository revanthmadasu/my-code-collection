package design_stack_overflow;

public interface Post {
    void upVote();
    void downVote();
    void comment(String comment, User user);
}
