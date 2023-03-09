package model.programState;
import exceptions.ADTException;
import exceptions.ExpressionEvaluationException;
import exceptions.StatementExecutionException;
import model.structures.IDictionary;
import model.structures.IList;
import model.structures.IStack;
import model.structures.IHeap;
import model.statements.IStatement;
import model.values.Value;

import java.io.BufferedReader;

public class ProgramState {
    private IStack<IStatement> exeStack;
    private IDictionary<String, Value> symTable;
    private IList<Value> out;
    private IDictionary<String, BufferedReader> fileTable;
    private IHeap heap;
    private IStatement originalProgram;
    private int id;
    private static int lastId = 0;

    public ProgramState(IStack<IStatement> exeStack, IDictionary<String, Value> symTable, IList<Value> out, IDictionary<String, BufferedReader> fileTable, IHeap heap, IStatement originalProgram) {
        this.exeStack = exeStack;
        this.symTable = symTable;
        this.out = out;
        this.fileTable = fileTable;
        this.heap = heap;
        this.originalProgram = originalProgram.deepCopy();
        this.exeStack.push(this.originalProgram);
        this.id = setId();
    }
    public ProgramState(IStack<IStatement> exeStack, IDictionary<String, Value> symTable, IList<Value> out, IDictionary<String, BufferedReader> fileTable, IHeap heap){
        this.exeStack = exeStack;
        this.symTable = symTable;
        this.out = out;
        this.fileTable = fileTable;
        this.heap = heap;
        this.id = setId();
    }

    public synchronized int setId(){
        lastId++;
        return lastId;
    }
    public boolean isNotCompleted(){
        return exeStack.isEmpty();
    }

    public ProgramState oneStep() throws StatementExecutionException, ExpressionEvaluationException, ADTException{
        if(exeStack.isEmpty())
            throw new StatementExecutionException("Empty program state stack!");
        IStatement currentStatement = exeStack.pop();
        return currentStatement.execute(this);
    }

    public IStack<IStatement> getExeStack() {
        return exeStack;
    }
    public void setExeStack(IStack<IStatement> exeStack) {
        this.exeStack = exeStack;
    }

    public IDictionary<String, Value> getSymTable() {
        return symTable;
    }
    public void setSymTable(IDictionary<String, Value> symTable) {
        this.symTable = symTable;
    }
    public IList<Value> getOut() {
        return out;
    }
    public void setOut(IList<Value> out) {
        this.out = out;
    }
    public IDictionary<String, BufferedReader> getFileTable(){
        return fileTable;
    }
    public IHeap getHeap(){
        return heap;
    }
    public void setHeap(IHeap newHeap){
        this.heap = newHeap;
    }

    public void setFileTable(IDictionary<String, BufferedReader> newFileTable) {
        this.fileTable = newFileTable;
    }

    public IStatement getOriginalProgram() {
        return originalProgram;
    }
    public void setOriginalProgram(IStatement originalProgram) {
        this.originalProgram = originalProgram;
    }
    public String exeStackToString(){
        return exeStack.toString();
    }
    public String symTableToString(){
        return symTable.toString();
    }
    public String outListToString(){
        return out.toString();
    }
    public String fileTableToString(){
        return fileTable.toString();
    }
    public String heapToString(){return heap.toString();}

    public String toString(){
        return "Id:" + id + "\n" +
                "Execution stack: \n" + exeStack + "\n" +
                "Symbol table: \n" + symTable + "\n" +
                "File table : \n" + fileTable + "\n" +
                "Heap: \n" + heap + "\n" +
                "Output list: \n" + out + "\n";
    }
}
