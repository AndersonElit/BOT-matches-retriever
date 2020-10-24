#include<stdio.h>
#include<string.h>
#include "char_storage.h"

//initialize empty array
void Array_Init(Array *array) {

    char *char_pointer;
    char_pointer = (char *)malloc(sizeof(char));

    if ( char_pointer == NULL ) {
        printf("Unable to allocate memory, exiting.\n");
        free(char_pointer);
        exit(0);
    } else {
        array->array = char_pointer;
        array->size = 0;
    }

}

void Array_Add(Array *array, char item) {

    char *char_pointer;
    array->size += 1;
    char_pointer = (char *)realloc(array->array, array->size * sizeof(char));

    if( char_pointer == NULL ) {
        printf("Unable to reallocate memory, exiting.\n");
        free(char_pointer);
        exit(0);
    } else {
        array->array = char_pointer;
        array->array[array->size-1] = item;
    }

}

void Array_Free(Array *array) {

    free(array->array);
    array->array = NULL;
    array->size = 0;

}
