package model.expression;
import exceptions.ADTException;
import exceptions.ExpressionEvaluationException;
import model.structures.IDictionary;
import model.structures.IHeap;
import model.types.RefType;
import model.types.Type;
import model.values.RefValue;
import model.values.Value;

public class ReadHeapExpression implements IExpression{
    private final IExpression expression;

    public ReadHeapExpression(IExpression expression){
        this.expression = expression;
    }

    @Override
    public Type typeCheck(IDictionary<String, Type> typeEnv) throws ExpressionEvaluationException, ADTException {
        Type type = expression.typeCheck(typeEnv);
        if(type instanceof RefType){
            RefType refType = (RefType) type;
            return refType.getInner();
        }else
            throw new ExpressionEvaluationException("The type of the expression is not a reference type");
    }

    @Override
    public Value eval(IDictionary<String, Value> symTable, IHeap heap) throws ExpressionEvaluationException, ADTException {
        Value value = expression.eval(symTable, heap);
        if(!(value instanceof RefValue)){
            throw new ExpressionEvaluationException(String.format("%s is not a reference value!", value));
        }
        RefValue refValue = (RefValue) value;
        return heap.get(refValue.getAddress());
    }

    @Override
    public IExpression deepCopy(){
        return new ReadHeapExpression(expression.deepCopy());
    }
    @Override
    public String toString(){
        return String.format("readHeap(%s)", expression);
    }

}
