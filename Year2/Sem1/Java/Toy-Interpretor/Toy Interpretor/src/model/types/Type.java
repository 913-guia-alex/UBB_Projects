package model.types;
import model.values.Value;

public interface Type {
    boolean equals(Type anotherType);
    Type deepCopy();
    Value defaultValue();
}
