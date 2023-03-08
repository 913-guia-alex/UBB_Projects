package model.types;

import model.values.BoolValue;
import model.values.Value;

public class BoolType implements Type{
    @Override
    public boolean equals(Type anotherType){
        return anotherType instanceof BoolType;
    }

    @Override
    public Type deepCopy(){
        return new BoolType();
    }
    public Value defaultValue(){
        return new BoolValue(false);
    }
    @Override
    public String toString(){
        return "bool";
    }
}
