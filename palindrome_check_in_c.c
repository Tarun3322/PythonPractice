#include <stdio.h>
#include <string.h>

int main() {
    char word[100];
    printf("Enter the word: ");
    scanf("%s", word);
    int count = 0;

    int l = strlen(word);

    for (int i = 0;i <= l/2; i++){
        if (word[i] == word[l-(i+1)]){
            count += i;
        } else {
            count = 0;
        }
    }

    if(count > 0){
        printf("True");
    } else {
        printf("False");
    }
    return 0;
}