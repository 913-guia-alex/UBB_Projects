package model.structures;
import exceptions.ADTException;
import java.util.List;
import java.util.function.Consumer;

public interface IList<T> {
    void add(T value);
    T pop() throws ADTException;
    boolean isEmpty();
    List<T> getAll();
}
