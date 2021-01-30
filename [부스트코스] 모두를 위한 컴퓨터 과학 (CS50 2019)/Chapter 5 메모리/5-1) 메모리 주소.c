#include <stdio.h>

int main(void)
{
    int n = 50;
    printf("%p\n", &n);
}
/*result
0x7fff547f0fcc
*/

//-----------------------//

#include <stdio.h>

int main(void)
{
    int n = 50;
    printf("%i\n", *&n);
}
/*result
50
*/