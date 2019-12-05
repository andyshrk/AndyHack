obj-m := hello.o
KDIR := /home/andy/WorkSpace/linux-next
all:
	make -C $(KDIR) M=$(PWD) modules
clean:
	make -C $(KDIR) M=$(PWD) clean
