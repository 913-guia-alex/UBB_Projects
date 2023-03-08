package model.statements;
import exceptions.ADTException;
import exceptions.ExpressionEvaluationException;
import exceptions.StatementExecutionException;
import model.programState.ProgramState;
import model.structures.IDictionary;
import model.types.Type;

public interface IStatement {
    ProgramState execute(ProgramState state) throws StatementExecutionException, ExpressionEvaluationException, ADTException;
    IStatement deepCopy();
    IDictionary<String, Type> typeCheck(IDictionary<String, Type> typeEnv) throws StatementExecutionException, ExpressionEvaluationException, ADTException;
}
