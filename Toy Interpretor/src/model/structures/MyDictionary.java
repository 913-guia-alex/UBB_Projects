package model.structures;
import exceptions.ADTException;
import java.util.Collection;
import java.util.HashMap;
import java.util.Set;
import java.util.Map;

public class MyDictionary<T1,T2> implements IDictionary<T1, T2> {
    HashMap<T1, T2> dictionary;

    public MyDictionary(){
        this.dictionary = new HashMap<>();
    }
    @Override
    public boolean isDefined(T1 key){
        return this.dictionary.containsKey(key);
    }
    @Override
    public T2 lookUp(T1 key) throws ADTException{
        if(!isDefined(key))
            throw new ADTException(key + " is not found");
        return this.dictionary.get(key);
    }
    @Override
    public void update(T1 key, T2 value) throws ADTException{
        if(!isDefined(key))
            throw new ADTException(key + " is not found");
        this.dictionary.put(key, value);
    }
    @Override
    public Collection<T2> values(){
        return this.dictionary.values();
    }

    @Override
    public boolean containsKey(T1 key) {
        return dictionary.containsKey(key);
    }
    @Override
    public void remove(T1 key) throws ADTException{
        if(!isDefined(key))
            throw new ADTException(key + " is not found");
        this.dictionary.remove(key);
    }
    public Set<T1> keySet(){
        return dictionary.keySet();
    }
    public String toString(){
        return this.dictionary.toString();
    }
    @Override
    public void put(T1 key, T2 value){
        this.dictionary.put(key, value);
    }
    @Override
    public Map<T1, T2> getContent(){
        return dictionary;
    }

    @Override
    public IDictionary<T1, T2> deepCopy() throws ADTException {
        IDictionary<T1, T2> toReturn = new MyDictionary<>();
        for (T1 key: keySet())
            toReturn.put(key, lookUp(key));
        return toReturn;
    }
}
