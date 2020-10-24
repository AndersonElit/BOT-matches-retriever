#ifndef STORAGE_H
#define STORAGE_H

#ifdef __cplusplus
extern "c" {
#endif

    typedef struct {

        char *array;
        size_t size;

    } Array;

    void Array_Init(Array *array);
    void Array_Add(Array *array, char item);
    void Array_Free(Array *array);

#ifdef __cplusplus
}
#endif

#endif
