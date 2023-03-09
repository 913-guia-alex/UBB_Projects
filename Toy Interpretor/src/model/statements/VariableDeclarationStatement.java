package model.statements;
import exceptions.ADTException;
import exceptions.ExpressionEvaluationException;
import exceptions.StatementExecutionException;
import model.programState.ProgramState;
import model.structures.IDictionary;
import model.values.Value;
import model.types.Type;

public class VariableDeclarationStatement implements IStatement{
    String name;
    Type type;

    public VariableDeclarationStatement(String name, Type type) {
        this.name = name;
        this.type = type;
    }
    @Override
    public ProgramState execute(ProgramState state) throws ADTException, ExpressionEvaluationException, StatementExecutionException{
        IDictionary<String,Value> symTable = state.getSymTable();
        if(symTable.containsKey(name)){
            throw new StatementExecutionException("Variable " + name + " has already been declared");
        }
        else{
            symTable.put(name, type.defaultValue());
        }
        state.setSymTable(symTable);
        return state;
    }

    @Override
    public IDictionary<String, Type> typeCheck(IDictionary<String, Type> typeEnv) throws StatementExecutionException, ExpressionEvaluationException, ADTException {
        typeEnv.put(name, type);
        return typeEnv;
    }

    @Override
    public IStatement deepCopy(){
        return new VariableDeclarationStatement(name, type);
    }
    public String toString(){
        return type.toString() + " " + name;
    }
}
