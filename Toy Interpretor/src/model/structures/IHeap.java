package model.structures;

import exceptions.ADTException;
import model.values.Value;
import java.util.HashMap;
import java.util.Set;

public interface IHeap {
    int getFreeValue();
    HashMap<Integer, Value> getContent();
    void setContent(HashMap<Integer, Value> newMap);
    int add(Value value);
    void update(Integer position, Value value) throws ADTException;
    Value get(Integer position) throws ADTException;
    boolean containsKey(Integer position);
    Set<Integer> keySet();
    void remove(Integer key) throws ADTException;
}
