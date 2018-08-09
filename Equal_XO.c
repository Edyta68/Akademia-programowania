#include <string.h>
#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
/**
* Function checks if a string has the same amount of 'x' and 'o's. Function must be case insensitive.
*/
bool XO(const char *word, const int length)
{
    int howManyX=0;
    int howManyO=0;

    for (int i=0; i<length; i++)
    {
        if(tolower(word[i])=='x')
        {
            howManyX++;
        }

        if (tolower(word[i])=='o')
        {
            howManyO++;
        }
    }

    if (howManyX==howManyO)
    {
        return true;
    }

    return false;
}

void test_cases()
{
	bool answer = XO("ooxx", strlen("ooxx"));
	assert(answer == true);

	answer = XO("xooxx", strlen("xooxx"));
	assert(answer == false);

	answer = XO("ooxXm", strlen("ooxXm"));
	assert(answer == true);

	answer = XO("zzoo", strlen("zzoo"));
	assert(answer == false);
}

int main(int argc, char *argv[])
{
	test_cases();
	return 0;
}
