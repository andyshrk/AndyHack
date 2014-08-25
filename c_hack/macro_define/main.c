#include <stdio.h>

#define SQR(x) printf("the square of "#x" if %d\n", (x)*(x))
#define XNAME(x) x##x
int main()
{
	
	SQR(8);
	printf(" the 8's name is XNAME(8)\n");
	return 0;
}
