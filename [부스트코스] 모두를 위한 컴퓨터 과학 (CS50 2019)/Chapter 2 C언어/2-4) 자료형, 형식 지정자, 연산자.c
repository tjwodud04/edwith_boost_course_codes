#include <stdio.h>

int main(void)
{
    int age;
    printf("what's your age?\n");
    scanf("%d", &age);
    printf("Your are at least %d days old.\n", age * 365);
}
/*example result
what's your age?
13
Your are at least 4745 days old.
*/

//----------------------------------//

#include <stdio.h>

int main(void)
{
    float price;
    printf("What's the price?\n");
    scanf("%f", &price);
    printf("Your total is %.2f\n", price * 1.0625);
}
/*example result
What's the price?
1700
Your total is 1806.25
*/