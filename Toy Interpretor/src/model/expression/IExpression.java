package model.expression;
import exceptions.ADTException;
import exceptions.ExpressionEvaluationException;
import model.structures.IDictionary;
import model.structures.IHeap;
import model.values.Value;
import model.types.Type;

public interface IExpression {

    Type typeCheck(IDictionary<String, Type> typeEnv) throws ExpressionEvaluationException, ADTException;
    Value eval(IDictionary<String, Value> symbolTable, IHeap heap) throws ExpressionEvaluationException, ADTException;
    IExpression deepCopy();
}
