#include <stdio.h>
#include <string.h>
#include <stdlib.h>

static void
_op_copy_c_dp_neon(unsigned int c, unsigned int *d, int l) {
#define AP "COPY_C_DP_"
   unsigned int *e = d + l, *tmp;
   asm volatile (
      ".fpu neon					\n\t"

		"vdup.i32 	q0,	%[c]		\n\t"

		// Can we do 32 byte?
		"andS		%[tmp],	%[d], $0x1f	\n\t"
		"beq		"AP"quadstart		\n\t"

		// Can we do at least 16 byte?
		"andS		%[tmp], %[d], $0x4	\n\t"
		"beq		"AP"dualstart		\n\t"

	// Only once
	AP"singleloop:					\n\t"
		"vst1.32	d0[0],  [%[d]]		\n\t"
		"add		%[d], #4		\n\t"

	// Up to 3 times
	AP"dualstart:					\n\t"
		"sub		%[tmp], %[e], %[d]	\n\t"
		"cmp		%[tmp], #32		\n\t"
		"blt		"AP"loopout		\n\t"

	AP"dualloop:					\n\t"
		"vstr.32	d0, [%[d]]		\n\t"

		"add		%[d], #8		\n\t"
		"andS		%[tmp], %[d], $0x1f	\n\t"
		"bne		"AP"dualloop		\n\t"


	AP"quadstart:					\n\t"
		"sub		%[tmp], %[e], %[d]	\n\t"
		"cmp		%[tmp], #32		\n\t"
		"blt		"AP"loopout		\n\t"

		"vmov		q1, q0			\n\t"
		"sub		%[tmp],%[e],#31		\n\t"

	AP "quadloop:					\n\t"
		"vstm		%[d]!,	{d0,d1,d2,d3}	\n\t"

		"cmp		%[tmp], %[d]		\n\t"
                "bhi		"AP"quadloop		\n\t"


	AP "loopout:					\n\t"
		"cmp 		%[d], %[e]		\n\t"
                "beq 		"AP"done		\n\t"
		"sub		%[tmp],%[e], %[d]	\n\t"
		"cmp		%[tmp],$0x04		\n\t"
		"beq		"AP"singleloop2		\n\t"

	AP "dualloop2:					\n\t"
		"sub		%[tmp],%[e],#7		\n\t"
	AP "dualloop2int:				\n\t"
		"vstr.64	d0, [%[d]]		\n\t"

		"add		%[d], #8		\n\t"
		"cmp 		%[tmp], %[d]		\n\t"
		"bhi 		"AP"dualloop2int	\n\t"

		// Single ??
		"cmp 		%[e], %[d]		\n\t"
		"beq		"AP"done		\n\t"

	AP "singleloop2:				\n\t"
		"vst1.32	d0[0], [%[d]]		\n\t"

	AP "done:\n\t"
		// Output
		: [tmp] "=r" (tmp)
		// Input
		: [c] "r" (c), [e] "r" (e), [d] "r" (d)
		// Clobbered
		: "q0","q1","memory"


   );
}

int main(int argc, char *argv[])
{
    int data[1024];
    int i;
    
    memset( data, 0, sizeof(data) );
    
    _op_copy_c_dp_neon( 0xff0000, data, 1024 );
    
    for ( i = 0; i < 1024; i ++ )
    {
        if ( data[i] != 0xff0000 )
        {
            printf("Data error at data[%d]: 0x%08x\n", i, data[i] );
            break;
        }
    }
    
    if ( i == 1024 )
        printf("All data is set correctly\n");
    
    return 0;
}


