package repository;
import exceptions.ADTException;
import model.programState.ProgramState;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

public class Repository implements IRepository{
    private List<ProgramState> programStates;
    private final String logFilePath;

    public Repository(ProgramState programState, String logFilePath) throws IOException {
        this.logFilePath = logFilePath;
        this.programStates = new ArrayList<>();
        this.addProgram(programState);
        this.emptyLogFile();
    }

    @Override
    public List<ProgramState> getProgramList(){
        return this.programStates;
    }

    @Override
    public void addProgram(ProgramState programState){
        this.programStates.add(programState);
    }

    @Override
    public void setProgramStates(List<ProgramState> programStates){
        this.programStates = programStates;
    }
    @Override
    public void logPrgStateExec(ProgramState programState) throws IOException, ADTException{
        PrintWriter logFile;
        logFile = new PrintWriter(new BufferedWriter(new FileWriter(logFilePath, true)));
        logFile.println(programState.toString());
        logFile.close();
    }
    @Override
    public void emptyLogFile() throws IOException{
        PrintWriter logFile;
        logFile = new PrintWriter(new BufferedWriter(new FileWriter(logFilePath, false)));
        logFile.close();
    }

}
