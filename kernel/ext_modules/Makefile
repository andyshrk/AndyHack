obj-m := hello.o
CROSS=/home/andy/WorkSpace/prebuilts/gcc/linux-x86/aarch64/gcc-linaro-6.3.1-2017.05-x86_64_aarch64-linux-gnu/bin/aarch64-linux-gnu-
KDIR := /home/andy/WorkSpace/linux-next
CC:=$(CROSS)gcc
AR:=$(CROSS)ar
CPU_TYPE=arm64

all:
	make ARCH=$(CPU_TYPE) -C $(KDIR) M=$(PWD) modules
clean:
	make -C $(KDIR) M=$(PWD) clean
