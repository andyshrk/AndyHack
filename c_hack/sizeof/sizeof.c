#include<stdio.h>

int main()
{
	int *p = NULL;
	int a[100];
	unsigned long phy;
	printf("sizeof(p) = %ld \n", sizeof(p));
	printf("sizeof(*p) = %ld \n", sizeof(*p));
	printf("sizeof(a) = %ld \n", sizeof(a));
	printf("sizeof(a[100]) = %ld \n", sizeof(a[100]));
	printf("sizeof(&a) = %ld \n", sizeof(&a));
	printf("sizeof(&a[0]) = %ld \n", sizeof(&a[0]));
	printf("sizeof(unsigned long) = %d\n", sizeof(phy));
	
	return 0;
}
