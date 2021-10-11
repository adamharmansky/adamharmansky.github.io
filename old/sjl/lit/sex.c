#include <stdio.h>
#include <string.h>

int
main()
{
	char* input;
	size_t size;
	getline(&input, &size, stdin);
	puts(input);
	if(!strncmp(input, "sex is what i like\n", 3)) printf("oh yeah man, I like sex too!\n");
}
