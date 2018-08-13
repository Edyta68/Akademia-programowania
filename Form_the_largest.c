#include <assert.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

/**
* Given a number, return the maximum number that could be formed with digits of the number given.
* For example: number = 7389, return 9873
*/
int form_the_largest_number(int number)
{
	int n = floor(log10(abs(number))) + 1;

	int *array = (int *)malloc(n * sizeof(int));

	for (int i = 0; i < n; i++)
	{
		array[i] = number % 10;
		number = number / 10;
	}

	for (int c = 0; c < n - 1; c++)
	{
		for (int d = 0; d < n - c - 1; d++)
		{
			if (array[d] > array[d + 1])
			{
				int swap = array[d];
				array[d] = array[d + 1];
				array[d + 1] = swap;
			}
		}
	}

	int wynik = 0;

	for (int i = 0; i < n; i++)
	{
		wynik += pow(10, i) * array[i];
	}

	return wynik;
}

void test_cases()
{
	int result = form_the_largest_number(213);
	assert(result == 321);

	result = form_the_largest_number(7389);
	assert(result == 9873);

	result = form_the_largest_number(63729);
	assert(result == 97632);

	result = form_the_largest_number(566797);
	assert(result == 977665);
}

int main()
{
	test_cases();
}