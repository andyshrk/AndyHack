#include<stdio.h>

int main(int argc, char *argv[])
{
	char buf[4] = {0x1f, 0x8b, 0x33, 0x55};
	unsigned int val = buf[1];

	printf("addr:%p %08x\n", buf, buf[0]);
	printf("%02x %02x %02x %02x\n", buf[0], buf[1], buf[2], buf[3]);
	printf("%p %p %p %p\n", &buf[0], &buf[1], &buf[2], &buf[3]);
	printf("%0x\n", val);

	return 0;
}
