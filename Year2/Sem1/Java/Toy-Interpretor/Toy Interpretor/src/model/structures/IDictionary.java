package model.structures;
import exceptions.ADTException;

import java.util.Collection;
import java.util.Set;
import java.util.Map;

public interface IDictionary<T1,T2> {
    boolean isDefined(T1 key);
    void put(T1 key, T2 value);
    boolean containsKey(T1 key);
    T2 lookUp(T1 key) throws ADTException;
    void remove(T1 key) throws ADTException;
    void update(T1 key, T2 value) throws ADTException;
    Set<T1> keySet();
    Map<T1, T2> getContent();
    Collection<T2> values();
    IDictionary<T1, T2> deepCopy() throws ADTException;
}
