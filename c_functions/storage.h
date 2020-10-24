#ifndef STORAGE_H
#define STORAGE_H

#ifdef __cplusplus
extern "c" {
#endif

    typedef struct {

        int *array;
        size_t size;

    } Array;

    void Array_Init(Array *array);
    void Array_Add(Array *array, int item);
    void Array_Free(Array *array);

#ifdef __cplusplus
}
#endif

#endif
