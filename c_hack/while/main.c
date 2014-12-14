#include<stdio.h>

unsigned int cnt = 10;

int main(void)
{
	while (cnt--) {
		printf("loop in while: %d\n", cnt);
	}

	printf("while loop end:%d \n", cnt);

	return 0;
}
