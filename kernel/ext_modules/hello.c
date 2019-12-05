#include <linux/module.h>
#include <linux/init.h>
#include <linux/kernel.h>
 
static int __init hello_init(void)
{
	      printk(KERN_WARNING "hello world.\n");
	            return 0;
}
static void __exit hello_exit(void)
{
	      printk(KERN_WARNING "hello exit!\n");
}
module_init(hello_init);
module_exit(hello_exit);
MODULE_LICENSE("GPL");
MODULE_AUTHOR("baoli");
MODULE_DESCRIPTION("hello world module");
 

