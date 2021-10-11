#include <stdio.h>
#include <string.h>

int main()
{
	char input[128];
	scanf("%s", input);
	char output[strlen(input)];
	printf("%d\n", (int)strlen(input));
	for(int i = 0;i < strlen(input); i++)
	{
		if(i%2 == 0)	output[(int)(i/2)] = input[i];
		else		output[strlen(input) - (int)(i/2) - 1] = input[i];
	}
	for(int i = 0; i < strlen(input); i++)
	{
		putchar(output[i]);
	}
	putchar('\n');
}
