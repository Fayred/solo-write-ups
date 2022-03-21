#include <stdio.h>

int main(){
    unsigned int random_N = 0x4b0a1705; // number 1

    unsigned int number2 = (random_N - 3) * 3;
    if( (number2 & 1) != 0)
        number2 = number2 - 1;
    unsigned int number3 = (int)number2 / 2 + 7;

    printf("%d %d %d", random_N, number2, number3);
    return 0;
}
