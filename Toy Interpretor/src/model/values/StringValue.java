package model.values;
import model.types.StringType;
import model.types.Type;

public class StringValue implements Value {
    private final String value;

    public StringValue(String value){
        this.value = value;
    }
    @Override
    public Type getType(){
        return new StringType();
    }
    @Override
    public boolean equals(Object value){
        if(!(value instanceof StringValue))
            return false;
        StringValue castValue = (StringValue) value;
        return this.value.equals(castValue.value);
    }

    @Override
    public Value deepCopy(){
        return new StringValue(value);
    }
    public String getValue(){
        return this.value;
    }
    @Override
    public String toString(){
        return "\"" + this.value + "\"";
    }
}
