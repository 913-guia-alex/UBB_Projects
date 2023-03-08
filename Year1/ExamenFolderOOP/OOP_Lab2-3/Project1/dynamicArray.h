#ifndef A23_911_GUIA_ALEX_DYNAMIC_ARRAY_H
#define A23_911_GUIA_ALEX_DYNAMIC_ARRAY_H
#pragma once
#include "domain.h"

typedef struct {
    Country* data;
    int capacity;
    int length;
}DynamicArray;

DynamicArray createDynamicArray(int capacity);
void destroyDynamicArray(DynamicArray* array);
void addElement(DynamicArray* array, Country element);
void deleteElement(DynamicArray* array, int delete_index);
void updateElement(DynamicArray* array, int update_index, Country update_element);
//void resizeDynamicArray(DynamicArray * array);
int arrayCapacity(DynamicArray* array);
int arrayLength(DynamicArray* array);


#endif //A23_911_GUIA_ALEX_DYNAMIC_ARRAY_H