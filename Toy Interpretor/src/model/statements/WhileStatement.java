package model.statements;

import exceptions.ADTException;
import exceptions.StatementExecutionException;
import exceptions.ExpressionEvaluationException;
import model.expression.IExpression;
import model.programState.ProgramState;
import model.structures.IDictionary;
import model.types.BoolType;
import model.structures.IStack;
import model.types.Type;
import model.values.BoolValue;
import model.values.Value;


public class WhileStatement implements IStatement{
    private final IExpression expression;
    private final IStatement statement;

    public WhileStatement(IExpression expression, IStatement statement){
        this.expression = expression;
        this.statement = statement;
    }

    @Override
    public ProgramState execute(ProgramState state) throws StatementExecutionException, ExpressionEvaluationException, ADTException{
        Value value = expression.eval(state.getSymTable(), state.getHeap());
        IStack<IStatement> stack = state.getExeStack();
        if(!(value.getType().equals(new BoolType())))
            throw new StatementExecutionException(String.format("Expression %s is not a boolean value!", value));
        BoolValue boolValue = (BoolValue) value;
        if(boolValue.getValue()){
            stack.push(this);
            stack.push(statement);

        }
        return state;
    }

    @Override
    public IDictionary<String, Type> typeCheck(IDictionary<String, Type> typeEnv) throws StatementExecutionException, ExpressionEvaluationException, ADTException {
        Type typeExp = expression.typeCheck(typeEnv);
        if(typeExp.equals(new BoolType())){
            statement.typeCheck(typeEnv.deepCopy());
            return typeEnv;
        }else
            throw new StatementExecutionException(String.format("The condition of WHILE is not of type bool"));
    }

    @Override
    public IStatement deepCopy() {
        return new WhileStatement(expression.deepCopy(), statement.deepCopy());
    }

    @Override
    public String toString(){
        return String.format("while(%s) {%s}", expression, statement);
    }
}
