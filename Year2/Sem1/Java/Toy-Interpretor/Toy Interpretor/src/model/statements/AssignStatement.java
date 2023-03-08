package model.statements;
import exceptions.ADTException;
import exceptions.ExpressionEvaluationException;
import exceptions.StatementExecutionException;
import model.programState.ProgramState;
import model.expression.IExpression;
import model.types.Type;
import model.structures.IDictionary;
import model.values.Value;

public class AssignStatement  implements IStatement{
    private final String key;
    private final IExpression expression;

    public AssignStatement(String key, IExpression expression) {
        this.key = key;
        this.expression = expression;
    }

    @Override
    public ProgramState execute(ProgramState state) throws ADTException, ExpressionEvaluationException, StatementExecutionException{
        IDictionary<String, Value> symbolTable = state.getSymTable();
        if(symbolTable.isDefined(key)){
            Value value = expression.eval(symbolTable, state.getHeap());
            Type type = (symbolTable.lookUp(key)).getType();
            if(value.getType().equals(type)){
                symbolTable.update(key, value);
            }
            else{
                throw new StatementExecutionException("Declared type of variable " + key + " and type of the assigned expression are not the same");
            }
        }else{
            throw new StatementExecutionException("The used variable " + key + " has not been declared before");
        }
        state.setSymTable(symbolTable);
        return state;
    }

    @Override
    public IDictionary<String, Type> typeCheck(IDictionary<String, Type> typeEnv) throws StatementExecutionException, ExpressionEvaluationException, ADTException {
        Type typeVar = typeEnv.lookUp(key);
        Type typeExp = expression.typeCheck(typeEnv);
        if(typeVar.equals(typeExp))
            return typeEnv;
        else
            throw new StatementExecutionException("Assignment: right hand side and left hand side have different types");
    }

    @Override
    public IStatement deepCopy(){
        return new AssignStatement(key, expression.deepCopy());
    }
    @Override
    public String toString(){
        return key + " = " + expression.toString();
    }

}
