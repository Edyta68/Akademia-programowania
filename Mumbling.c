#include <string.h>
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
/**
* Function duplicates letters based on their index. Each index means how many times the letter needs to be duplicated.
* See test cases for examples.
*/

char* accumulate(const char *word, const int length)
{
    int wordId=0;
    char* retWord=(char*)malloc(wordLn+1);
    int wordLn=length*(length+1)/2+length-1;
    retWord[wordLn]='\0';
    for(int i=0; i<length; i++)
    {
        retWord[wordId]=toupper(word[i]);
        wordId++;

        for(int j=0; j<i; j++)
        {
            retWord[wordId]=tolower(word[i]);
            wordId++;
        }

        if (i<length-1)
        {
            retWord[wordId]='-';
            wordId++;
        }
    }

    return retWord;

}

void test_cases()
{
	char* result = accumulate("abcd", strlen("abcd"));
	assert(strcmp(result, "A-Bb-Ccc-Dddd") == 0);

	result = accumulate("cwAt", strlen("cwAt"));
	assert(strcmp(result, "C-Ww-Aaa-Tttt") == 0);
}

int main(int argc, char *argv[])
{
	test_cases();
	return 0;
}
