package model.expression;
import exceptions.ADTException;
import exceptions.ExpressionEvaluationException;
import model.structures.IDictionary;
import model.structures.IHeap;
import model.types.Type;
import model.values.Value;

public class VariableExpression implements IExpression{
    String key;

    public VariableExpression(String key){
        this.key = key;
    }

    @Override
    public Type typeCheck(IDictionary<String, Type> typeEnv) throws ExpressionEvaluationException, ADTException {
        return typeEnv.lookUp(key);
    }

    @Override
    public Value eval(IDictionary<String, Value> symbolTable, IHeap heap) throws ADTException, ExpressionEvaluationException{
        return symbolTable.lookUp(key);
    }
    @Override
    public IExpression deepCopy(){
        return new VariableExpression(key);
    }
    @Override
    public String toString(){
        return key;
    }
}
