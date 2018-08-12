#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

/**
* Function returns an array of 5 elements.
* Those 5 elements are created randomly in the range 1 - 49.
* Numbers can't repeat.
*/
int* Lotto_drawing()
{
	
	int number;
	int howMany = 5;
	int currNumber = 0;
	int *result = (int*)malloc(howMany * sizeof(int));
	bool isOk;

	for (int i = 0; i < howMany; i++)
	{
		do
		{
			number = rand() % 49 + 1;
			isOk = true;

			for (int j = 0; j < currNumber; j++)
			{
				if (number == result[j])
				{
					isOk = false;
					break;
				}
			}

			if (isOk == true)
			{
				result[currNumber] = number;
				currNumber++;
			}

			else
				continue;

		} while (!isOk);
	}

	return result;
}

/* Please create test cases for this program. test_cases() function can return void, bool or int. */

void test_cases()
{
	for (int testing = 0; testing<100; testing++) 
	{
		int* result = Lotto_drawing();
		for (int i = 0; i<4; i++) 
		{
			for (int j = i + 1; j<5; j++) 
			{
				assert(result[i] != result[j]);
			}
			assert(result[i] >= 1 && result[i] <= 49);
		}
	}
}


int main()
{
	srand(time(NULL));
	test_cases();
}


