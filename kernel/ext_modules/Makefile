obj-m := hello.o
CROSS=/usr/local/toolchain/arm-gnu-toolchain-14.2.rel1-x86_64-aarch64-none-linux-gnu/bin/aarch64-none-linux-gnu-
KDIR := /home/andy/WorkSpace/linux-next
CC:=$(CROSS)gcc
AR:=$(CROSS)ar
CPU_TYPE=arm64

all:
	make ARCH=$(CPU_TYPE) CROSS_COMPILE=$(CROSS) -C $(KDIR) M=$(PWD) modules
clean:
	make -C $(KDIR) M=$(PWD) clean
