package repository;
import exceptions.ADTException;
import model.programState.ProgramState;
import java.io.IOException;
import java.util.List;

public interface IRepository {
    List<ProgramState> getProgramList();
    void setProgramStates(List<ProgramState> programStates);
    ProgramState getCurrentState();
    void addProgram(ProgramState program);
    void logPrgStateExec() throws IOException, ADTException;
    void emptyLogFile() throws IOException;
}
