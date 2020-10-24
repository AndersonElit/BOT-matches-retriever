#include<stdio.h>
#include<string.h>
#include "storage.h"

/*initialize empty array*/
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

/*

char * getChartList(char str[]) {

    // count number of chars
    //char * string;
    //string = str;//"Hola soy anderson como van todos";
    char * token = strtok(str, " ");
    int count = 0;

    while( token != NULL ) {
        printf("%s\n", token );
        count++;
        token = strtok(NULL, " ");
    }

    //store each char into an array
    char * arr[count];
    //char * string2;
    //string2 = str; //"Hola soy anderson como van todos";
    char * token2 = strtok(str, " ");
    int i = 0;

    while( token2 != NULL ) {
        arr[i] = token2;
        i++;
        token2 = strtok(NULL, " ");
    }

    char * val1;
    val1 = arr[3];

    return val1;

}

*/

int main() {

    /*
    // count number of chars
    char string[] = "Hola soy anderson como van todos";
    char * token = strtok(string, " ");
    int count = 0;

    while( token != NULL ) {
        count++;
        token = strtok(NULL, " ");
    }

    //store each char into an array
    char * arr[count];
    char string2[] = "Hola soy anderson como van todos";
    char * token2 = strtok(string2, " ");
    int i = 0;

    while( token2 != NULL ) {
        arr[i] = token2;
        i++;
        token2 = strtok(NULL, " ");
    }

    printf("%s", arr[5]);
    */

    /*

    char chain[] = "Hola soy anderson como van todos";
    char * value1;
    value1 = getChartList(chain);

    //printf("%s", value1);
    */

    Array pointers;
    int i;

    Array_Init(&pointers);

    for (i = 0; i < 10; i++) {
        Array_Add(&pointers, i);
    }

    for (i = 0; i < pointers.size; i++) {
        printf("Value: %d Size:%d \n", pointers.array[i], pointers.size);
    }

    Array_Free(&pointers);

    return 0;

}
