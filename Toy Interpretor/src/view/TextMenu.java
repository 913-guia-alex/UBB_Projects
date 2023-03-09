package view;
import exceptions.ADTException;
import model.structures.MyDictionary;
import model.structures.IDictionary;
import java.util.Scanner;

public class TextMenu {
    private IDictionary<String, Command> commands;

    public TextMenu(){
        this.commands = new MyDictionary<>();
    }
    public void addCommand(Command command){
        this.commands.put(command.getKey(), command);
    }
    private void printMenu(){
        for(Command command: commands.values()){
            String line = String.format("%4s: %s", command.getKey(), command.getDescription());
            System.out.println(line);
        }
    }
    public void show(){
        Scanner scanner = new Scanner(System.in);
        while(true){
            printMenu();
            System.out.println("Input the option: ");
            String key = scanner.nextLine();
            try{
                Command command = commands.lookUp(key);
                command.execute();
            }catch(ADTException exception){
                System.out.println("Invalid option");
            }
        }
    }
}
