// Right Triangle
#include <stdio.h>

int main() {

    int a;
    printf("Enter the number: ");
    scanf("%d", &a);

    for (int i = 1; i <= a; i++ ){
        for (int j = 1; j <= i; j++){
            printf("* ");
        }
        printf("\n");
    }
    return 0;
}

// Reverse Triangle
#include <stdio.h>

int main() {

    int a;
    printf("Enter the number: ");
    scanf("%d", &a);

    for (int i = a; i >= 1; i-- ){
        for (int j = 1; j <= i; j++){
            printf("* ");
        }
        printf("\n");
    }
    return 0;
}

// Basic Triangle
#include <stdio.h>

int main()
{
    int a ;
    printf("Enter the Number: ");
    scanf("%d", &a);
    printf("\n");

    for (int i = 1; i <= a; i++){
        for (int j = 1; j <= a-i; j++){
            printf("  ");
        }

        for (int k = 1; k <= ( 2 * i - 1); k++){
            printf("* ");
        }
        printf("\n");
    }

    return 0;
}
