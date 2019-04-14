#include<stdio.h>
#include <string.h>

static void _op_copy_c_dp_neon(unsigned int c, unsigned int *d, int l) {
	unsigned int *e = d + l;
	unsigned tmp;
	unsigned *d2;
	asm volatile (
			"mov  %[tmp],	%[c]		\n\t"
		"copy_loop:				\n\t"
			"str  %[tmp],  	[%[d]]		\n\t"
			"add  %[d], 	#4		\n\t"
			"cmp  %[d],	%[e]		\n\t"
			"blt  copy_loop			\n\t"
			:[tmp] "+r" (tmp), [d] "+r" (d), [e] "+r" (e)
			:[c] "r" (c)
			: "memory"
		     );
}

static int op_add(int a, int b)
{
	int result;
	asm volatile (
			"add %[result],	%[a],	%[b]		\n\t"
			: [result] "=r" (result)
			: [a] "r" (a), [b] "b" (b)
			);
	return result;
}

int main(void)
{
	int data[64];
	int i;

	memset(data, 0, sizeof(data));

	_op_copy_c_dp_neon(0xff0000, data, 64);

	for ( i = 0; i < 64; i ++ )
	{
		if (data[i] != 0xff0000)
		{
			printf("Data error at data[%d]: 0x%08x\n", i, data[i] );
			break;
		}
	}

	if ( i == 64 )
		printf("All data is set correctly\n");

	return 0;
}
