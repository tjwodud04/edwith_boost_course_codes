
///좋아하는 동물을 알려주세요"로 질문하여 동물 이름을 animal이라는 변수에 저장하고,
///이를 "내가 좋아하는 동물은"으로 출력해주는 코드를 작성해보세요.

#include <stdio.h>

main(void)
{
    char animal[100];
    printf("좋아하는 동물을 알려주세요. \n");
    scanf("%s", animal);
    printf("내가 좋아하는 동물은 %s \n", animal);
}

/* example result
좋아하는 동물을 알려주세요. 
하마
내가 좋아하는 동물은 하마
*/
