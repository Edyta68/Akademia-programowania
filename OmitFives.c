#include <string.h>
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int numbers_without_five(int start, int end)
{
    int count=0;
    int curr=start;


    for(int i=start; i<=end; i++)
    {
        int curr2=i;
        int is5=0;
            while (curr2>0)
            {
                if (curr2%10 == 5)
                {
                    is5=1;
                    break;
                }


            curr2/=10;
            }

        if(is5==0)
        {
            count++;
        }

    }
        return count;
}




void test_cases()
{
	int answer = numbers_without_five(4, 8);
	assert(answer == 4);

	answer = numbers_without_five(1, 9);
	assert(answer == 8);

	answer = numbers_without_five(4, 17);
	assert(answer == 12);
}

int main(int argc, char *argv[])
{

	test_cases();
	return 0;
}
