#include <stdio.h>
#include <string.h>

struct employee_details{

    int id;
    float salary;
    char name[30];

}e1;

int main(){

    printf("Do you want to Enter the Employee details? \'Yes\' or \'No\': ");

    char a[5], b[5];

    scanf("%s", a);

    for (int i = 0; a[i] != '\0'; i++) {
        b[i] = tolower(a[i]);
    }

    if(!strcmp(b, "yes")){

        printf("\nPlease Enter Employee ID:");
        scanf("%d", &e1.id);

        printf("Please Enter Employee Name:");
        scanf("%s", e1.name);

        printf("Please Enter Employee Salary:");
        scanf("%f", &e1.salary);

    } else {

        printf("Thank You!");

    }

    printf("\nPlease find the below Employee details you entered: \n");
    printf("ID: %d", e1.id);
    printf("\nName: %s", e1.name);
    printf("\nSalary: %0.2f", e1.salary);
}