package model.expression;
import exceptions.ADTException;
import exceptions.ExpressionEvaluationException;
import model.types.BoolType;
import model.types.IntType;
import model.types.Type;
import model.structures.IDictionary;
import model.structures.IHeap;
import model.values.BoolValue;
import model.values.Value;
import java.util.Objects;

public class LogicExpression implements IExpression{
    IExpression expression1;
    IExpression expression2;
    String operation;

    public LogicExpression(IExpression expression1, IExpression expression2, String operation){
        this.expression1 = expression1;
        this.expression2 = expression2;
        this.operation = operation;
    }
    @Override
    public Type typeCheck(IDictionary<String, Type> typeEnv) throws ExpressionEvaluationException, ADTException{
        Type type1, type2;
        type1 = expression1.typeCheck(typeEnv);
        type2 = expression2.typeCheck(typeEnv);
        if (type1.equals(new BoolType())){
            if (type2.equals(new BoolType())){
                return new BoolType();
            }else
                throw new ExpressionEvaluationException("Second operand is not a boolean");
        }else
            throw new ExpressionEvaluationException("First operand is not a boolean");

    }

    @Override
    public Value eval(IDictionary<String, Value> symbolTable, IHeap heap) throws ExpressionEvaluationException, ADTException {
        Value value1, value2;
        value1 = this.expression1.eval(symbolTable, heap);
        if (value1.getType().equals(new BoolType())) {
            value2 = this.expression2.eval(symbolTable, heap);
            if (value2.getType().equals(new BoolType())) {
                BoolValue bool1 = (BoolValue) value1;
                BoolValue bool2 = (BoolValue) value2;
                boolean b1, b2;
                b1 = bool1.getValue();
                b2 = bool2.getValue();
                if (Objects.equals(this.operation, "and")) {
                    return new BoolValue(b1 && b2);
                } else if (Objects.equals(this.operation, "or")) {
                    return new BoolValue(b1 || b2);
                }
            } else {
                throw new ExpressionEvaluationException("Second operand is not a boolean!");
            }
        } else {
            throw new ExpressionEvaluationException("First operand is not a boolean!");
        }
        return null;
    }
    @Override
    public IExpression deepCopy(){
        return new LogicExpression(expression1.deepCopy(), expression2.deepCopy(), operation);
    }
    public String toString(){
        return expression1.toString() + " " + operation + " " + expression2.toString();
    }
}
