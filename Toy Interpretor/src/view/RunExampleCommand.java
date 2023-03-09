package view;
import controller.Controller;
import exceptions.ADTException;
import exceptions.ExpressionEvaluationException;
import exceptions.StatementExecutionException;
import java.io.IOException;
import java.util.Scanner;
import java.util.Objects;

public class RunExampleCommand extends Command{
    private final Controller controller;

    public RunExampleCommand(String key, String description, Controller controller){
        super(key, description);
        this.controller = controller;
    }

    @Override
    public void execute(){
        try{
            System.out.println("Display the steps?(yes/no)");
            Scanner option = new Scanner(System.in);
            String optionString = option.next();
            controller.setDisplayFlag(Objects.equals(optionString, "yes"));
            controller.allStep();
        }catch(ExpressionEvaluationException | ADTException | StatementExecutionException | IOException | InterruptedException exception){
            System.out.println(exception.getMessage());
        }
    }
}
