#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i = 0;
    int j;
    char *input = "mjqjpqmgbljsphdztnvjfqwrcgsmlb";
    char *signal = NULL;

    while (input[i])
    {
        j = 0;
        signal = malloc(sizeof(char) * 4);
        if (!signal)
            return (-1);
        //extract set
        while (input[i + j] && j < 3)
        {
            signal[j] = input[i + j];
            j++;
        }
        signal[j] = '\0';
        //check if current char is in set
        char current_char = input[i + j];
        printf("set = %s & current char = %c\n", signal, current_char);
        j = 0;
        while(signal[j] && signal[j] != current_char)
            j++;
        if (!signal[j])
        {

            break;
        }
        else
            free(signal);
        i++;
    }
    printf("count = %d, char = %c\n", i + j + 1, input[i+j]);
    return (0);
}