package model.statements;
import exceptions.ADTException;
import exceptions.ExpressionEvaluationException;
import exceptions.StatementExecutionException;
import model.programState.ProgramState;
import model.structures.IDictionary;
import model.structures.IStack;
import model.structures.IStack;
import model.types.Type;

import java.util.Stack;

public class CompoundStatement implements IStatement{
    IStatement firstStatement;
    IStatement secondStatement;

    public CompoundStatement(IStatement firstStatement, IStatement secondStatement) {
        this.firstStatement = firstStatement;
        this.secondStatement = secondStatement;
    }

    @Override
    public ProgramState execute(ProgramState state) throws ADTException, ExpressionEvaluationException, StatementExecutionException{
        IStack<IStatement> stack = state.getExeStack();
        stack.push(secondStatement);
        stack.push(firstStatement);
        state.setExeStack(stack);
        return state;
    }

    @Override
    public IDictionary<String, Type> typeCheck(IDictionary<String, Type> typeEnv) throws StatementExecutionException, ExpressionEvaluationException, ADTException {
        return secondStatement.typeCheck(firstStatement.typeCheck(typeEnv));
    }

    @Override
    public IStatement deepCopy(){
        return new CompoundStatement(firstStatement.deepCopy(), secondStatement.deepCopy());
    }
    @Override
    public String toString(){
        return "(" + firstStatement.toString() + "; " + secondStatement.toString() + ")";
    }
}
