package model.structures;
import exceptions.ADTException;
import java.util.List;

public interface IStack<T> {
    T pop() throws ADTException;
    void push(T value);
    T peek();
    boolean isEmpty();
    List<T> getAllReverse();
}
