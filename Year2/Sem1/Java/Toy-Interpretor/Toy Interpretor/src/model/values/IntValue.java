package model.values;
import model.types.IntType;
import model.types.Type;

public class IntValue implements Value{
    private final int value;

    public IntValue(int value){
        this.value = value;
    }
    @Override
    public Type getType(){
        return new IntType();
    }
    @Override
    public boolean equals(Object value){
        if(!(value instanceof IntValue))
            return false;
        IntValue castValue = (IntValue) value;
        return this.value == castValue.value;
    }

    @Override
    public Value deepCopy(){
        return new IntValue(value);
    }
    public int getValue(){
        return this.value;
    }
    @Override
    public String toString(){
        return Integer.toString(this.value);
    }
}
