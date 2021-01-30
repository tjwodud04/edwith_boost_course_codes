#include <stdio.h>

int main(void)
{
    int numbers[] = {4, 8, 15, 16, 23, 42};

    for (int i = 0; i < 6; i++)
    {
        if (numbers[i] == 50)
        {
            printf("Found\n");
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}
/*result
Not found
exit status 1
*/

//--------------------------------------//

#include <stdio.h>
#include <string.h>

int main(void)
{
    char *names[] = {"EMMA", "RODRIGO", "BRIAN", "DAVID"};
    char *numbers[] = {"617–555–0100", "617–555–0101", "617–555–0102", "617–555–0103"};

    for (int i = 0; i < 4; i++)
    {
        if (strcmp(names[i], "EMMA") == 0)
        {
            printf("Found %s\n", numbers[i]);
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}
/*result
Found 617–555–0100
*/

//---------------------------------------//

#include <stdio.h>
#include <string.h>

typedef struct
{
    char *name;
    char *number;
} person;

int main(void)
{
    person people[4];

    people[0].name = "EMMA";
    people[0].number = "617–555–0100";
    people[1].name = "RODRIGO";
    people[1].number = "617–555–0101";
    people[2].name = "BRIAN";
    people[2].number = "617–555–0102";
    people[3].name = "DAVID";
    people[3].number = "617–555–0103";

    for (int i = 0; i < 4; i++)
    {
        if (strcmp(people[i].name, "EMMA") == 0)
        {
            printf("Found %s\n", people[i].number);
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}
/*result
Found 617–555–0100
*/