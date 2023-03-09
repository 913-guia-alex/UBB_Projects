package model.structures;
import exceptions.ADTException;
import java.util.List;
import java.util.Arrays;
import java.util.Collections;
import java.util.Stack;

public class MyStack<T> implements IStack<T>{
    Stack<T> stack;

    public MyStack(){
        this.stack = new Stack<>();
    }
    @Override
    public T pop() throws ADTException{
        if(stack.isEmpty())
            throw new ADTException("Empty stack");
        return this.stack.pop();
    }
    @Override
    public void push(T value){
        this.stack.push(value);
    }
    @Override
    public T peek(){
        return this.stack.peek();
    }
    @Override
    public String toString(){
        return this.stack.toString();
    }
    @Override
    public boolean isEmpty(){
        return this.stack.isEmpty();
    }
    @Override
    public List<T> getAllReverse(){
        List<T> list = Arrays.asList((T[]) stack.toArray());
        Collections.reverse(list);
        return list;
    }

}

