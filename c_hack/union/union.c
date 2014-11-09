#include <stdio.h>

int main()
{
	union reg_ptr {
		int *p32;
		char *p8;
	};

	union reg_ptr regs;
	regs.p32  = (int *)0xff940000;
	printf("p8:%p p32+1:%p p8+1:%p\n",regs.p8, regs.p32 + 1, regs.p8 + 1);
	return 0;
	
}
