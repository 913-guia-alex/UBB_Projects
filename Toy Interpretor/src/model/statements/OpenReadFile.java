package model.statements;
import exceptions.ADTException;
import exceptions.ExpressionEvaluationException;
import exceptions.StatementExecutionException;
import model.programState.ProgramState;
import model.expression.IExpression;
import model.types.StringType;
import model.structures.IDictionary;
import model.types.Type;
import model.values.StringValue;
import model.values.Value;

import javax.swing.plaf.nimbus.State;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;

public class OpenReadFile implements IStatement{
    private final IExpression expression;

    public OpenReadFile(IExpression expression) {
        this.expression = expression;
    }
    @Override
    public ProgramState execute(ProgramState state) throws StatementExecutionException, ExpressionEvaluationException, ADTException{
        Value value = expression.eval(state.getSymTable(), state.getHeap());
        if(value.getType().equals(new StringType())){
            StringValue filename = (StringValue) value;
            IDictionary<String, BufferedReader> fileTable = state.getFileTable();
            if(!fileTable.isDefined(filename.getValue())){
                BufferedReader br;
                try{
                    br = new BufferedReader(new FileReader(filename.getValue()));
                }catch(FileNotFoundException e){
                    throw new StatementExecutionException("The file could not be opened");
                }
                fileTable.put(filename.getValue(), br);
                state.setFileTable(fileTable);
            }else{
                throw new StatementExecutionException("The file is already open");
            }
        }else{
            throw new StatementExecutionException("The expression is not a string");
        }
        return state;
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
        return new OpenReadFile(expression.deepCopy());
    }
    @Override
    public String toString(){
        return "open(" + expression.toString() + ")";
    }
}
