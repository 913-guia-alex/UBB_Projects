package model.statements;
import exceptions.ADTException;
import exceptions.ExpressionEvaluationException;
import exceptions.StatementExecutionException;
import model.programState.ProgramState;
import model.structures.IDictionary;
import model.structures.IList;
import model.expression.IExpression;
import model.types.Type;
import model.values.Value;

public class PrintStatement implements IStatement{
    IExpression expression;

    public PrintStatement(IExpression expression) {
        this.expression = expression;
    }
    @Override
    public ProgramState execute(ProgramState state) throws ADTException, ExpressionEvaluationException, StatementExecutionException{
        IList<Value> out = state.getOut();
        out.add(expression.eval(state.getSymTable(), state.getHeap()));
        state.setOut(out);
        return state;
    }

    @Override
    public IDictionary<String, Type> typeCheck(IDictionary<String, Type> typeEnv) throws StatementExecutionException, ExpressionEvaluationException, ADTException {
        expression.typeCheck(typeEnv);
        return typeEnv;
    }

    @Override
    public IStatement deepCopy(){
        return new PrintStatement(expression.deepCopy());
    }
    @Override
    public String toString(){
        return "print(" + expression.toString() + ")";
    }
}
