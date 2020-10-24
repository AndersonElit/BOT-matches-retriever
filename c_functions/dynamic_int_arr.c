#include<stdio.h>
#include<string.h>
#include "storage.h"

//initialize empty array
void Array_Init(Array *array) {

    int *int_pointer;
    int_pointer = (int *)malloc(sizeof(int));

    if ( int_pointer == NULL ) {
        printf("Unable to allocate memory, exiting.\n");
        free(int_pointer);
        exit(0);
    } else {
        array->array = int_pointer;
        array->size = 0;
    }

}

void Array_Add(Array *array, int item) {

    int *int_pointer;
    array->size += 1;
    int_pointer = (int *)realloc(array->array, array->size * sizeof(int));

    if(int_pointer == NULL) {
        printf("Unable to reallocate memory, exiting.\n");
        free(int_pointer);
        exit(0);
    } else {
        array->array = int_pointer;
        array->array[array->size-1] = item;
    }

}

void Array_Free(Array *array) {

    free(array->array);
    array->array = NULL;
    array->size = 0;

}
