// Square

#include <stdio.h>

int main()
{
    int n;

    printf("Enter the number of rows: ");
    scanf("%d", &n);
    printf("\n");

    for (int i =0 ; i <= n; i++ ){

        for (int j = 0; j <=n; j++){

            printf("* ");

        }

        printf("\n");

    }
}

// Reverse Right Triangle

#include <stdio.h>

int main()
{
    int n;

    printf("Enter the number of rows: ");
    scanf("%d", &n);
    printf("\n");

    for (int i =0 ; i < n; i++ ){

        for (int j = i; j < n; j++){

            printf("* ");

        }

        printf("\n");

    }
}

// Tilted Straight Right Triangle

#include <stdio.h>

int main()
{
    int n;

    printf("Enter the number of rows: ");
    scanf("%d", &n);
    printf("\n");

    for (int i = n; i > 0; i--){

        for (int j = i - 1; j > 0; j--){

            printf("  ");

        }

        for (int j = i; j <=n; j++){

            printf("* ");

        }

        printf("\n");

    }
}


// Straight Right Triangle

#include <stdio.h>

int main()
{
    int n;

    printf("Enter the number of rows: ");
    scanf("%d", &n);
    printf("\n");

    for (int i = n ; i > 0; i-- ){

        for (int j = i; j <= n; j++){

            printf("* ");

        }

        printf("\n");

    }
}

// Straight Basic Triangle

#include <stdio.h>

int main()
{
    int n;

    printf("Enter the number of rows: ");
    scanf("%d", &n);
    printf("\n");

    for (int i = n; i > 0; i--){

        for (int j = i - 1; j > 0; j--){

            printf("  ");

        }

        for (int j = i; j <= n; j++){

            printf("* ");

        }

        for (int j = i+1; j <= n; j++){

            printf("* ");

        }

        printf("\n");

    }
}