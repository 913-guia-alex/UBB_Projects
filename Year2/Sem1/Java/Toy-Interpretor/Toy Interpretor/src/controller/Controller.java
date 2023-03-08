package controller;
import exceptions.ADTException;
import exceptions.ExpressionEvaluationException;
import exceptions.StatementExecutionException;
import model.programState.ProgramState;
import model.statements.IStatement;
import repository.IRepository;
import model.structures.IStack;
import model.values.RefValue;
import model.values.Value;
import java.io.IOException;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Controller {
    IRepository repository;
    boolean displayFlag = false;

    public void setDisplayFlag(boolean displayFlag) {
        this.displayFlag = displayFlag;
    }
    public Controller(IRepository repository) {
        this.repository = repository;
    }

    public List<Integer> getAddrFromSymTable(Collection<Value> symTableValues){
        return symTableValues.stream()
                .filter(v -> v instanceof RefValue)
                .map(v -> {RefValue v1 = (RefValue)v; return v1.getAddress();})
                .collect(Collectors.toList());
    }

    public List<Integer> getAddrFromHeap(Collection<Value> heapValues){
        return heapValues.stream()
                .filter(v -> v instanceof RefValue)
                .map(v -> {RefValue v1 = (RefValue)v; return v1.getAddress();})
                .collect(Collectors.toList());
    }
    public Map<Integer, Value> safeGarbageCollector(List<Integer> symTableAddr, List<Integer> heapAddr, Map<Integer, Value> heap){
        return heap.entrySet().stream()
                .filter(e -> (symTableAddr.contains(e.getKey()) || heapAddr.contains(e.getKey())))
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
    }

    public ProgramState oneStep(ProgramState state) throws ADTException, ExpressionEvaluationException, StatementExecutionException{
        IStack<IStatement> stack = state.getExeStack();
        if(stack.isEmpty())
            throw new StatementExecutionException("Empty program state stack!");
        IStatement currentStatement = stack.pop();
        state.setExeStack(stack);
        return currentStatement.execute(state);
    }

    public void allSteps() throws ExpressionEvaluationException, ADTException, StatementExecutionException, IOException{
        ProgramState state = this.repository.getCurrentState();
        this.repository.logPrgStateExec();;
        display();
        while(!state.getExeStack().isEmpty()){
            oneStep(state);
            this.repository.logPrgStateExec();
            state.getHeap().setContent((HashMap<Integer, Value>) safeGarbageCollector(getAddrFromSymTable(state.getSymTable().getContent().values()), getAddrFromHeap(state.getHeap().getContent().values()), state.getHeap().getContent()));
            this.repository.logPrgStateExec();
            display();
        }
    }
    private void display(){
        if(displayFlag){
            System.out.println(this.repository.getCurrentState().toString());
        }
    }
}
