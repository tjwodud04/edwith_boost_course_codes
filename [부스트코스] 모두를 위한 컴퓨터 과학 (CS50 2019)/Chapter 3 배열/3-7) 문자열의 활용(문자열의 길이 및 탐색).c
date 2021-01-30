#include <stdio.h>
#include <string.h>

int main(void)
{
    char s[100];
    printf("Input: ");
    scanf("%s", s);
    printf("Output:\n");
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        printf("%c\n", s[i]);
    }
}
/*example result
Input: literal
Output:
l
i
t
e
r
a
l
*/