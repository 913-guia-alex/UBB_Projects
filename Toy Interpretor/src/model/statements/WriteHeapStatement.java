package model.statements;
import exceptions.ADTException;
import exceptions.StatementExecutionException;
import exceptions.ExpressionEvaluationException;
import model.expression.IExpression;
import model.programState.ProgramState;
import model.structures.IDictionary;
import model.structures.IHeap;
import model.types.RefType;
import model.types.Type;
import model.values.RefValue;
import model.values.Value;

public class WriteHeapStatement implements IStatement{
    private final String varName;
    private final IExpression expression;

    public WriteHeapStatement(String varName, IExpression expression){
        this.varName = varName;
        this.expression = expression;
    }

    @Override
    public ProgramState execute(ProgramState state) throws StatementExecutionException, ExpressionEvaluationException, ADTException{
        IDictionary<String, Value> symTable = state.getSymTable();
        IHeap heap = state.getHeap();
        if(!symTable.isDefined(varName)){
            throw new StatementExecutionException(String.format("Variable %s is not in the symbTable", varName));
        }
        Value value = symTable.lookUp(varName);
        if(!(value instanceof RefValue)){
            throw new StatementExecutionException(String.format("Variable %s is not a reference value", varName));
        }
        RefValue refValue = (RefValue) value;
        Value evaluated = expression.eval(symTable, heap);
        if(!evaluated.getType().equals(refValue.getLocationType())){
            throw new StatementExecutionException(String.format("Variable %s is not of type %s", varName, evaluated.getType()));
        }
        heap.update(refValue.getAddress(), evaluated);
        state.setHeap(heap);
        return state;
    }

    @Override
    public IDictionary<String, Type> typeCheck(IDictionary<String, Type> typeEnv) throws StatementExecutionException, ExpressionEvaluationException, ADTException {
        if(typeEnv.lookUp(varName).equals(new RefType(expression.typeCheck(typeEnv))))
            return typeEnv;
        else
            throw new StatementExecutionException(String.format("Variable %s is not of type RefType(%s)", varName, expression.typeCheck(typeEnv)));
    }

    @Override
    public IStatement deepCopy(){
        return new WriteHeapStatement(varName, expression.deepCopy());
    }
    @Override
    public String toString(){
        return String.format("writeHeap(%s, %s)", varName, expression);
    }
}

