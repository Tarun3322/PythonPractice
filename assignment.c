#include <stdio.h>
#include <time.h>

struct Structure{
    
    int a[4][3][2];
    int var;


};


int main() {

    int var = RandomArrayValues();

    printf("var = %d \n",var);

    if (var%10 == 0){

        printf("\n");
        goto pattern;

    }

pattern: Pattern();


return 0;

}

int Pattern(){

    for (int i = 1; i <= 5; i++ ){
        for (int j = 1; j <= i; j++){
            printf("%c",'a' + j-1);
        }
    printf("\n");
    }
}



int RandomArrayValues(){

    struct Structure s;
    int *ptr;
    ptr = &s.a[0][0][0];

    srand(time(0));

    printf("Random values: \n");
    for (int i=0 ; i<4 ; i++){
        for (int j=0 ; j<3 ; j++){
            for (int k=0 ; k<2 ; k++){
                s.a[i][j][k] = rand()%100;
                printf("Value of a[%d][%d][%d]: ", i,j,k);
                printf("%d \n", s.a[i][j][k]);
            }
        }
    }

    printf("\nPrinting the 3D Arrays:\n");

    for (int i=0 ; i<4 ; i++){
        for (int j=0 ; j<3 ; j++){
            for (int k=0 ; k<2 ; k++){
                printf("%d ", *ptr);
                if (k==1){
                    printf("\n");
                }
                if (i==1 && j==1 && k==1){
                    s.var = *ptr;
                }
                ptr++;
            }
        }
    printf("\n");
    }

    printf("\n");

    return s.var;

}