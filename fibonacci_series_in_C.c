#include <stdio.h>

int main() {
    int n ;
    printf("Number of Terms: ");
    scanf("%d", &n);
    
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
