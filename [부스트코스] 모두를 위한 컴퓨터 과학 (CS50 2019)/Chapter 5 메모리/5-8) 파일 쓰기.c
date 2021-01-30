#include <stdio.h>
#include <string.h>

int main(void)
{
    FILE *file = fopen("phonebook.csv", "a");
    char *name;
    printf("Name: ");
    scanf("%s", name);
    char *number;
    printf("Number: ");
    scanf("%s", number);
    fprintf(file, "%s,%s\n", name, number);
    fclose(file);
}