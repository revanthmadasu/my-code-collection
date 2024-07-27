package design_stack_overflow;

import java.util.ArrayList;
import java.util.HashMap;

public class Question implements Post {
    private static int questionCount = 0;
    private static HashMap<Integer, Question>  questionsMap = new HashMap<Integer, Question>();
    public String question;
    private ArrayList<Answer> answers;
    private ArrayList<Comment> comments;
    int upVoteCount, downVoteCount;
    int id;
    public static Question getQuestion(int id) {
        return Question.questionsMap.get(id);
    }
    public static Question[] getQuestions(int start, int end) {
        return (Question[]) Question.questionsMap.values().stream().skip(start-1).limit(end - start).toArray();
    }
    Question(String question) {
        this.question = question;
        this.downVoteCount = 0;
        this.upVoteCount = 0;
        this.answers = new ArrayList<>();
        this.comments = new ArrayList<>();
        Question.questionCount += 1;
        this.id = Question.questionCount;
        Question.questionsMap.put(this.id, this);
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

    public Answer answer(String answer, User user) {
        Answer ans = new Answer(answer, user);
        this.answers.add(ans);
        return ans;
    }

    public Answer[] getAnswers(int start, int end) {
        return (Answer[]) this.answers.subList(start, end).toArray();
    }

    public Comment[] getComments(int start, int end) {
        return (Comment[]) this.comments.subList(start, end).toArray();
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Question: " + question + "\n");
        sb.append("\t Answers: \n");
        for(Answer ans: this.answers) {
            sb.append(String.format("\t\t%s\n", ans));
        }
        sb.append("\t Comments: \n");
        for(Comment comment: this.comments) {
            sb.append(String.format("\t\t%s\n", comment));
        }
        return sb.toString();
    }

}
