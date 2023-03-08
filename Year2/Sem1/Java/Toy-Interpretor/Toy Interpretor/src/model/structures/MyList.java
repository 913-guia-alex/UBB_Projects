package model.structures;
import exceptions.ADTException;
import java.util.List;
import java.util.ArrayList;
import java.util.function.Consumer;

public class MyList<T> implements IList<T>{
    List<T> list;

    public MyList(){
        this.list = new ArrayList<>();
    }
    @Override
    public void add(T value){
        this.list.add(value);
    }
    @Override
    public T pop() throws ADTException{
        if(list.isEmpty())
            throw new ADTException("Empty list");
        return this.list.remove(0);
    }
    @Override
    public boolean isEmpty(){
        return this.list.isEmpty();
    }
    @Override
    public List<T> getAll(){
        return list;
    }
    @Override
    public String toString(){
        return this.list.toString();
    }
}
