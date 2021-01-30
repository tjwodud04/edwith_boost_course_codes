#include <stdio.h>

int main(void)
{
    char *s = "EMMA";
    printf("%p\n\n", s);
    printf("%p\n", &s[0]);
    printf("%p\n", &s[1]);
    printf("%p\n", &s[2]);
    printf("%p\n\n", &s[3]);
    printf("%c\n", *s);
    printf("%c\n", *(s + 2));
    printf("%c\n", *(s + 1));
    printf("%c\n", *(s + 3));
}
/*result
0x400694

0x400694
0x400695
0x400696
0x400697

E
M
M
A
*/
//---------------------------------//

#include <stdio.h>
#include <string.h>

int main(void)
{
    char s[100];
    char t[100];
    printf("s: ");
    scanf("%s", s);
    printf("t: ");
    scanf("%s", t);

    int compare = strcmp(s, t);

    if (compare == 0)
    {
        printf("Same\n");
    }
    else
    {
        printf("Different\n");
    }
}
/*example result
s: salang
t: salang
Same
s: solang
t: salang
Different
*/