package model.statements;
import exceptions.ADTException;
import exceptions.ExpressionEvaluationException;
import exceptions.StatementExecutionException;
import model.expression.IExpression;
import model.programState.ProgramState;
import model.types.IntType;
import model.types.StringType;
import model.structures.IDictionary;
import model.types.Type;
import model.values.IntValue;
import model.values.StringValue;
import model.values.Value;
import java.io.BufferedReader;
import java.io.IOException;

public class ReadFile implements IStatement{
    private final IExpression expression;
    private final String variableName;

    public ReadFile(IExpression expression, String variableName) {
        this.expression = expression;
        this.variableName = variableName;
    }
    @Override
    public ProgramState execute(ProgramState state) throws StatementExecutionException, ExpressionEvaluationException, ADTException{
        IDictionary<String, Value> symbolTable = state.getSymTable();
        IDictionary<String, BufferedReader> fileTable = state.getFileTable();
        if(symbolTable.isDefined(variableName)){
            Value value = symbolTable.lookUp(variableName);
            if(value.getType().equals(new IntType())){
                value = expression.eval(symbolTable, state.getHeap());
                if(value.getType().equals(new StringType())){
                    StringValue castValue = (StringValue) value;
                    if(fileTable.isDefined(castValue.getValue())){
                        BufferedReader br = fileTable.lookUp(castValue.getValue());
                        try{
                            String line = br.readLine();
                            if(line == null)
                                line = "0";
                            symbolTable.put(variableName, new IntValue(Integer.parseInt(line)));
                        }catch(IOException e){
                            throw new StatementExecutionException("The file could not be read");
                        }
                    }else{
                        throw new StatementExecutionException(String.format("The file table does not contain %s", castValue));
                    }
                }else{
                    throw new StatementExecutionException("The expression is not a string");
                }
            }else{
                throw new StatementExecutionException("The variable is not an integer");
            }
        }else{
            throw new StatementExecutionException("The variable is not defined in the symTable");
        }
        return state;
    }

    @Override
    public IDictionary<String, Type> typeCheck(IDictionary<String, Type> typeEnv) throws StatementExecutionException, ExpressionEvaluationException, ADTException {
        if(expression.typeCheck(typeEnv).equals(new StringType()))
            if(typeEnv.lookUp(variableName).equals(new IntType()))
                return typeEnv;
            else
                throw new StatementExecutionException("The variable is not an integer");
        else
            throw new StatementExecutionException("The expression is not a string");
    }

    @Override
    public IStatement deepCopy(){
        return new ReadFile(expression.deepCopy(), variableName);
    }
    @Override
    public String toString(){
        return "read(" + expression.toString() + ", " + variableName + ")";
    }
}
