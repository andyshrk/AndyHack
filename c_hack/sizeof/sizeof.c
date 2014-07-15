#include<stdio.h>

int main()
{
	int *p = NULL;
	int a[100];
	printf("sizeof(p) = %ld \n", sizeof(p));
	printf("sizeof(*p) = %ld \n", sizeof(*p));
	printf("sizeof(a) = %ld \n", sizeof(a));
	printf("sizeof(a[100]) = %ld \n", sizeof(a[100]));
	printf("sizeof(&a) = %ld \n", sizeof(&a));
	printf("sizeof(&a[0]) = %ld \n", sizeof(&a[0]));
	
	return 0;
}
