#include <stdio.h>

int main() {

    fibonacci(11);

    return 0;
}

int fibonacci(int n){

    int a = 0, b = 1;

    printf("%d, %d, ", a, b);

    for (int i =3; i <= n; i++){
        int c = a + b;
        if (i == n) {
            printf("%d.",c);
        } else {
        printf("%d, ", c);
        a = b;
        b = c;}
    }

}

// Alternate Code

#include <stdio.h>

int fibonacci(){

    int n;
    printf("Enter the Number: ");
    scanf("%d", &n);

    return n;
}

int main() {

    int n = fibonacci();

    int a = 0, b = 1;

    printf("%d, %d, ", a, b);

    for (int i =3; i <= n; i++){
        int c = a + b;
        if (i == n) {
            printf("%d.",c);
        } else {
        printf("%d, ", c);
        a = b;
        b = c;}
    }

    return 0;
}
