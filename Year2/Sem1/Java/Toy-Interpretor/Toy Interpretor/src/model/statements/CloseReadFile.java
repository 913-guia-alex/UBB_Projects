package model.statements;
import exceptions.ADTException;
import exceptions.ExpressionEvaluationException;
import exceptions.StatementExecutionException;
import model.programState.ProgramState;
import model.expression.IExpression;
import model.types.StringType;
import model.structures.IDictionary;
import model.values.StringValue;
import model.values.Value;
import java.io.BufferedReader;
import java.io.IOException;
import model.types.Type;

public class CloseReadFile implements IStatement{
    private final IExpression expression;

    public CloseReadFile(IExpression expression) {
        this.expression = expression;
    }

    @Override
    public ProgramState execute(ProgramState state) throws StatementExecutionException, ExpressionEvaluationException, ADTException{
        Value value = expression.eval(state.getSymTable(), state.getHeap());
        if(!value.getType().equals(new StringType())){
            throw new StatementExecutionException("The expression is not a string");
        }
        StringValue fileName = (StringValue) value;
        IDictionary<String, BufferedReader> fileTable = state.getFileTable();
        if(!fileTable.isDefined(fileName.getValue())){
            throw new StatementExecutionException("The file is not open");
        }
        BufferedReader bufferedReader = fileTable.lookUp(fileName.getValue());
        try {
            bufferedReader.close();
        }catch (IOException e){
            throw new StatementExecutionException("The file could not be closed");
        }
        fileTable.remove(fileName.getValue());
        state.setFileTable(fileTable);
        return null;
    }

    @Override
    public IDictionary<String, Type> typeCheck(IDictionary<String, Type> typeEnv) throws StatementExecutionException, ExpressionEvaluationException, ADTException {
        if(expression.typeCheck(typeEnv).equals(new StringType()))
            return typeEnv;
        else
            throw new StatementExecutionException("The expression is not a string");
    }

    @Override
    public IStatement deepCopy(){
        return new CloseReadFile(expression.deepCopy());
    }
    @Override
    public String toString(){
        return "close(" + expression.toString() + ")";
    }
}
