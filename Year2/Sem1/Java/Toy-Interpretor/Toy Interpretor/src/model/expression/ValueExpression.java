package model.expression;
import exceptions.ADTException;
import exceptions.ExpressionEvaluationException;
import model.structures.IDictionary;
import model.structures.IHeap;
import model.values.Value;
import model.types.Type;

public class ValueExpression implements IExpression{
    Value value;

    public ValueExpression(Value value){
        this.value = value;
    }

    @Override
    public Type typeCheck(IDictionary<String, Type> typeEnv) throws ExpressionEvaluationException{
        return value.getType();
    }
    @Override
    public Value eval(IDictionary<String, Value> symbolTable, IHeap heap) throws ExpressionEvaluationException, ADTException{
        return this.value;
    }
    @Override
    public IExpression deepCopy(){
        return new ValueExpression(value);
    }
    @Override
    public String toString(){
        return this.value.toString();
    }
}
