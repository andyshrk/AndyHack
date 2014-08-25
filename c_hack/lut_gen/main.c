#include<stdio.h>
#define LUT_SIZE 1024
int main()
{
	int i=0;
	int val=0;
	for (i=0; i < LUT_SIZE; i++) {
		if (LUT_SIZE == 256)
			val = i + (i << 8) + (i << 16);
		else
			val = i + (i << 10) + (i << 20);
		if(!(i%10))
			printf("\n");
		printf("0x%08x ",val);
	}
	
	return 0;
}
