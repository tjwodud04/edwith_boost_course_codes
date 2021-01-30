#include <stdio.h>

const int N = 3;

int main(void)
{
    int scores[N];
    scores[0] = 72;
    scores[1] = 73;
    scores[2] = 33;

    printf("Average: %i\n", (scores[0] + scores[1] + scores[2]) / N);
}
/*result
Average: 59
*/