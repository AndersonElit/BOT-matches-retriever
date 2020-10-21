#include<stdio.h>
#include<string.h>

char getChartList(char str[]) {

    // count number of chars
    char * string;
    string = str;//"Hola soy anderson como van todos";
    char * token = strtok(string, " ");
    int count = 0;

    while( token != NULL ) {
        count++;
        token = strtok(NULL, " ");
    }

    //store each char into an array
    char * arr[count];
    char * string2;
    string2 = str; //"Hola soy anderson como van todos";
    char * token2 = strtok(string2, " ");
    int i = 0;

    while( token2 != NULL ) {
        arr[i] = token2;
        i++;
        token2 = strtok(NULL, " ");
    }

    return arr;

}

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

    char chain = "Hola soy anderson como van todos";
    char * archain;
    archain = getChartList(chain);

    printf("%s", archain[1]);

    return 0;

}
