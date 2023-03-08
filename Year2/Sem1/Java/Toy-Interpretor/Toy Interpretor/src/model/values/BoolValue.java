package model.values;
import model.types.BoolType;
import model.types.Type;

public class BoolValue implements Value{
    private final boolean value;

    public BoolValue(boolean value){
        this.value = value;
    }

    @Override
    public Type getType(){
        return new BoolType();
    }
    @Override
    public boolean equals(Object another){
        if(!(another instanceof BoolValue))
            return false;
        BoolValue castValue = (BoolValue) another;
        return this.value == castValue.value;
    }
    @Override
    public Value deepCopy(){
        return new BoolValue(value);
    }
    public boolean getValue(){
        return this.value;
    }
    @Override
    public String toString(){
        return this.value ? "true" : "false";
    }
}
