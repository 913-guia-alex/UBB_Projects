package model.statements;
import exceptions.ADTException;
import exceptions.ExpressionEvaluationException;
import exceptions.StatementExecutionException;
import model.expression.IExpression;
import model.programState.ProgramState;
import model.types.RefType;
import model.types.Type;
import model.structures.IDictionary;
import model.structures.IHeap;
import model.values.RefValue;
import model.values.Value;


public class NewStatement implements IStatement{
    private final String varName;
    private final IExpression expression;

    public NewStatement(String varName, IExpression expression){
        this.varName = varName;
        this.expression = expression;
    }

    @Override
    public ProgramState execute(ProgramState state) throws StatementExecutionException, ExpressionEvaluationException, ADTException{
        IDictionary<String, Value> symbolTable = state.getSymTable();
        IHeap heap = state.getHeap();
        if(!symbolTable.isDefined(varName)){
            throw new StatementExecutionException(String.format("Variable %s is not in the symbTable", varName));
        }
        Value varValue = symbolTable.lookUp(varName);
        if(!(varValue.getType() instanceof RefType)){
            throw new StatementExecutionException(String.format("Variable %s is not a reference type", varName));
        }
        Value evaluated = expression.eval(symbolTable, heap);
        Type locationType = ((RefValue)varValue).getLocationType();
        if(!locationType.equals(evaluated.getType())){
            throw new StatementExecutionException(String.format("Variable %s is not of type %s", varName, evaluated.getType()));
        }
        int newPosition = heap.add(evaluated);
        symbolTable.put(varName, new RefValue(newPosition, locationType));
        state.setSymTable(symbolTable);
        state.setHeap(heap);
        return state;
    }

    @Override
    public IDictionary<String, Type> typeCheck(IDictionary<String, Type> typeEnv) throws StatementExecutionException, ExpressionEvaluationException, ADTException {
        Type typeVar = typeEnv.lookUp(varName);
        Type typeExp = expression.typeCheck(typeEnv);
        if(typeVar.equals(new RefType(typeExp)))
            return typeEnv;
        else
            throw new StatementExecutionException("NewStatement: right hand side and left hand side have different types ");
    }

    @Override
    public IStatement deepCopy(){
        return new NewStatement(varName, expression.deepCopy());
    }
    @Override
    public String toString(){
        return String.format("New(%s, %s)", varName, expression);
    }

}
