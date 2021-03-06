/*
 * Simple app. to do memory accesses via /dev/mem.
 *
 * $Id: io.c,v 1.5 2000/08/21 09:01:57 richard Exp $
 *
 * Copyright (c) Richard Hirst <rhirst@linuxcare.com>
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <stdint.h>
#include <sys/stat.h>
#include <time.h>
#include <fcntl.h>
#include <errno.h>

#ifndef FALSE
#define FALSE	0
#define TRUE	(!FALSE)
#endif

#ifdef MMAP64
#define mmap mmap64
#endif

#define LOOPS		30000
static char *argv0;

static void
usage (void)
{
	fprintf(stderr,
"Raw memory i/o utility - $Revision: 1.5 $\n\n"
"%s -v -1|2|4 -r|w [-l <len>] [-f <file>] <addr> [<value>]\n\n"
"    -v         Verbose, asks for confirmation\n"
"    -1|2|4     Sets memory access size in bytes (default byte)\n"
"    -l <len>   Length in bytes of area to access (defaults to\n"
"               one access, or whole file length)\n"
"    -r|w       Read from or Write to memory (default read)\n"
"    -f <file>  File to write on memory read, or\n"
"               to read on memory write\n"
"    <addr>     The memory address to access\n"
"    <val>      The value to write (implies -w)\n\n"
"Examples:\n"
"    %s 0x1000                  Reads one byte from 0x1000\n"
"    %s 0x1000 0x12             Writes 0x12 to location 0x1000\n"
"    %s -2 -l 8 0x1000          Reads 8 words from 0x1000\n"
"    %s -r -f dmp -l 100 200    Reads 100 bytes from addr 200 to file\n"
"    %s -w -f img 0x10000       Writes the whole of file to memory\n"
"\n"
"Note access size (-1|2|4) does not apply to file based accesses.\n\n",
		argv0, argv0, argv0, argv0, argv0, argv0);
	exit(1);
}

uint64_t get_time_ns(void)
{
	struct timespec t;

	t.tv_sec = t.tv_nsec = 0;
	clock_gettime(CLOCK_MONOTONIC, &t);

	return t.tv_sec * 1000000000LL + t.tv_nsec;
}

static void read_test(const char *name, uint32_t *addr, uint32_t len)
{
        int loop = 10;
        uint32_t cnt = len;
        int i = 0;
        uint32_t *base = addr;
        uint64_t start, end;
        int64_t cost;
        uint32_t val;

	start = get_time_ns();
        for (loop=0; loop < LOOPS; loop++) {
                len = cnt;
                len >>= 2;
                for (i=0; i < len; i++)
                        asm volatile("ldr %0, %1" "\n\t"
                                     :"=r"(val)
                                     :"m"(base[i]));
        }
	end = get_time_ns();
        cost =  end - start;
	printf("%s read %ld bytes, time %lld ns ( %d MB / S)\n",
               name, cnt, cost, (LOOPS*(1000000000LL * cnt) >> 20) / cost);
}

static void memcpy_test(const char *name, uint32_t *src, uint32_t *dst, uint32_t len)
{
	int loop = 10; 
        uint64_t start, end;
        int64_t cost;

	start = get_time_ns();
	for (loop=0; loop < LOOPS; loop++) {
		memcpy(dst, src, len);
	}
	end = get_time_ns();
	cost =  end - start;
        printf("%s memcpy %ld bytes, time %lld ns ( %d MB / S)\n",
               name, len, cost, (LOOPS*(1000000000LL * len) >> 20) / cost);
}

//static void vmem_test(int length, int iosize, unsigned long value)
static void vmem_test(void)
{
	uint64_t start, end;
        int64_t cost;
        int i, val;
        int cnt;
	int len = cnt = 0x38000;
	uint8_t *addr = malloc(len);
	void * dst = malloc(len);
	uint32_t *base = (uint32_t *)addr;
	uint32_t loop = 0;


	if (!addr) {
		printf("malloc failed\n");
		return;
	}

	start = get_time_ns();
	for (loop = 0; loop < LOOPS; loop++) {
		len = cnt;
		len >>= 2;
		for (i=0; i < len; i++) {
			 base[i] = 0xaabbccdd;
		}
	}
	end = get_time_ns();
        cost = end - start;
        printf("vmem write  %ld bytes(iosize 4), time %lld ns ( %d MB / S)\n",
		cnt, cost, (LOOPS * (cnt * 1000000000LL) >> 20) / cost);
#if 0
	for (loop = 0; loop < 10; loop++) {
		len = cnt;
		len >>= 2;
		start = get_time_ns();
		for (i=0; i < len; i++)
		//	val = base[i];	
		asm volatile("ldr %0, %1" "\n\t"
			:"=r"(val)
			:"m"(base[i]));
		end = get_time_ns();

		cost = end - start;
		printf("val:%x vmem read  %ld bytes(iosize 4), time %lld ns ( %d MB / S)\n",
			val, cnt, cost, ((cnt * 1000000000LL) >> 20) / cost);
	}
#else
	read_test("vmem", base, cnt);
#endif
	memcpy_test("vmem", base, dst, len >> 2);	

}
static void memread_test(uint8_t *addr, int len, int iosize)
{
	uint64_t start, end;
	int64_t cost;
	int i, val;
	int cnt = len;

	start = get_time_ns();
	switch(iosize) {
		case 1:
			while (len) { 
				val = *(uint8_t *)addr;
				addr += iosize;
				len -= iosize;
			}
			break;
		case 2: 
			while (len) {
				val =  *(uint16_t *)addr;
				addr += iosize;
				len -= iosize;
			}
			break;
		case 4:
			while (len) {
				val =  *(uint32_t *)addr;
				addr += iosize;
				len -= iosize;
			}
			break;
	}
	end = get_time_ns();
	cost = end - start;
	printf("mmap read %ld bytes(iosize %d), time %lld ns ( %d MB / S)\n",
		cnt, iosize, cost, ((cnt * 1000000000LL) >> 20) / cost);
}
static void
memread_memory(unsigned long phys_addr, uint8_t *addr, int len, int iosize)
{
	int i;
	memread_test(addr, len, iosize);
#if 0
	while (len) {
		printf("%08lx: ", phys_addr);
		i = 0;
		while (i < 16 && len) {
			switch(iosize) {
			case 1:
				printf(" %02x", *(uint8_t *)addr);
				break;
			case 2:
				printf(" %04x", *(uint16_t *)addr);
				break;
			case 4:
				printf(" %08x", *(uint32_t *)addr);
				break;
			}
			i += iosize;
			addr += iosize;
			len -= iosize;
		}
		phys_addr += 16;
		printf("\n");
	}
#endif
}



static void
write_memory(uint8_t *addr, int len, int iosize, unsigned long value)
{
	int64_t start, end;
	int64_t cost;
	int cnt = len;
	uint32_t loop = 0;
	uint32_t *base = (uint32_t *)addr;
	void *dst = addr + (len >> 2); 
	int i;
	int val;

	//vmem_test(len, iosize, value);
	vmem_test();

	start = get_time_ns();
	for (loop = 0; loop < LOOPS; loop++) {
		len = cnt;
		addr = base;
		while (len) {
			*(uint32_t *)addr = value;
			len -= iosize;
			addr += iosize;
		}
	}
	end = get_time_ns();
        cost =  end - start;
        printf("mmp write %ld bytes(iosize %d), time %lld ns ( %d MB / S)\n",
               cnt, iosize, cost, (LOOPS * (1000000000LL * cnt) >> 20) / cost);
	read_test("mmap", base, cnt);
	memcpy_test("mmap", base, dst , cnt >> 2);

}


int
main (int argc, char **argv)
{
	int mfd, ffd = 0, req_len = 0, opt;
	uint8_t *real_io;
	unsigned long real_len, real_addr, req_addr, req_value = 0, offset;
	char *endptr;
	int memread = TRUE;
	int iosize = 1;
	char *filename = NULL;
	int verbose = 0;

	argv0 = argv[0];
	opterr = 0;
	if (argc == 1)
		usage();

	while ((opt = getopt(argc, argv, "hv124rwl:f:")) > 0) {
		switch (opt) {
		case 'h':
			usage();
		case 'v':
			verbose = 1;
			break;
		case '1':
		case '2':
		case '4':
			iosize = opt - '0';
			break;
		case 'r':
			memread = TRUE;
			break;
		case 'w':
			memread = FALSE;
			break;
		case 'l':
			req_len = strtoul(optarg, &endptr, 0);
			if (*endptr) {
				fprintf(stderr, "Bad <size> value '%s'\n", optarg);
				exit(1);
			}
			break;
		case 'f':
			filename = strdup(optarg);
			break;
		default:
			fprintf(stderr, "Unknown option: %c\n", opt);
			usage();
		}
	}

	if (optind == argc) {
		fprintf(stderr, "No address given\n");
		exit(1);
	}
	req_addr = strtoul(argv[optind], &endptr, 0);
	if (*endptr) {
		fprintf(stderr, "Bad <addr> value '%s'\n", argv[optind]);
		exit(1);
	}
	optind++;
	if (!filename && optind < argc)
		memread = FALSE;
	if (filename && optind > argc) {
		fprintf(stderr, "Filename AND value given\n");
		exit(1);
	}
	if (!filename && !memread && optind == argc) {
		fprintf(stderr, "No value given for WRITE\n");
		exit(1);
	}
	if (!filename && !memread) {
		req_value = strtoul(argv[optind], &endptr, 0);
		if (*endptr) {
			fprintf(stderr, "Bad <value> value '%s'\n", argv[optind]);
			exit(1);
		}
		if ((iosize == 1 && (req_value & 0xffffff00)) ||
				(iosize == 2 && (req_value & 0xffff0000))) {
			fprintf(stderr, "<value> too large\n");
			exit(1);
		}
		optind++;
	}
	if (filename && memread && !req_len) {
		fprintf(stderr, "No size given for file memread\n");
		exit(1);
	}
	if (optind < argc) {
		fprintf(stderr, "Too many arguments '%s'...\n", argv[optind]);
		exit(1);
	}
	if (filename && memread) {
		ffd = open(filename, O_WRONLY|O_CREAT|O_TRUNC, S_IRUSR|S_IWUSR|S_IRGRP|S_IROTH);
		if (ffd < 0) {
			fprintf(stderr, "Failed to open destination file '%s': %s\n", filename, strerror(errno));
			exit(1);
		}
	}
	if (filename && !memread) {
		ffd = open(filename, O_RDONLY);
		if (ffd < 0) {
			fprintf(stderr, "Failed to open source file '%s': %s\n", filename, strerror(errno));
			exit(1);
		}
	}

	if (filename && !req_len) {
		req_len = lseek(ffd, 0, SEEK_END);
		if (req_len < 0) {
			fprintf(stderr, "Failed to seek on '%s': %s\n",
					filename, strerror(errno));
			exit(1);
		}
		if (lseek(ffd, 0, SEEK_SET)) {
			fprintf(stderr, "Failed to seek on '%s': %s\n",
					filename, strerror(errno));
			exit(1);
		}
	}
	if (!req_len)
		req_len = iosize;

	if ((iosize == 2 && (req_addr & 1)) ||
			(iosize == 4 && (req_addr & 3))) {
		fprintf(stderr, "Badly aligned <addr> for access size\n");
		exit(1);
	}
	if ((iosize == 2 && (req_len & 1)) ||
			(iosize == 4 && (req_len & 3))) {
		fprintf(stderr, "Badly aligned <size> for access size\n");
		exit(1);
	}

	if (!verbose)
		/* Nothing */;
	else if (filename && memread)
		printf("Request to memread 0x%x bytes from address 0x%08lx\n"
			"\tto file %s, using %d byte accesses\n",
			req_len, req_addr, filename, iosize);
	else if (filename)
		printf("Request to write 0x%x bytes to address 0x%08lx\n"
			"\tfrom file %s, using %d byte accesses\n",
			req_len, req_addr, filename, iosize);
	else if (memread)
		printf("Request to memread 0x%x bytes from address 0x%08lx\n"
			"\tusing %d byte accesses\n",
			req_len, req_addr, iosize);
	else
		printf("Request to write 0x%x bytes to address 0x%08lx\n"
			"\tusing %d byte accesses of value 0x%0*lx\n",
			req_len, req_addr, iosize, iosize*2, req_value);

	real_addr = req_addr & ~4095;
	if (real_addr == 0xfffff000) {
		fprintf(stderr, "Sorry, cannot map the top 4K page\n");
		exit(1);
	}
	offset = req_addr - real_addr;
	real_len = req_len + offset;
	real_len = (real_len + 4095) & ~ 4095;
	if (real_addr + real_len < real_addr) {
		fprintf(stderr, "Aligned addr+len exceeds top of address space\n");
		exit(1);
	}
	if (verbose)
		printf("Attempting to map 0x%lx bytes at address 0x%08lx\n",
			real_len, real_addr);

	mfd = open("/dev/mem", O_RDWR);
	if (mfd == -1) {
		perror("open /dev/mem");
		exit(1);
	}
	if (verbose)
		printf("open(/dev/mem) ok\n");
	real_io = mmap(NULL, real_len,
			memread ? PROT_READ:PROT_WRITE,
			MAP_SHARED, mfd, real_addr);
	if (real_io == (void *)(-1)) {
		fprintf(stderr, "mmap() failed: %s\n", strerror(errno));
		exit(1);
	}
	if (verbose)
		printf("mmap() ok\n");

	if (verbose) {
		int c;

		printf("OK? ");
		fflush(stdout);
		c = getchar();
		if (c != 'y' && c != 'Y') {
			printf("Aborted\n");
			exit(1);
		}
	}

	if (filename && memread) {
		int n = write(ffd, real_io + offset, req_len);

		if (n < 0) {
			fprintf(stderr, "File write failed: %s\n", strerror(errno));
			exit(1);
		}
		else if (n != req_len) {
			fprintf(stderr, "Only wrote %d of %d bytes to file\n",
					n, req_len);
			exit(1);
		}
	}
	else if (filename) {
		int n = read(ffd, real_io + offset, req_len);

		if (n < 0) {
			fprintf(stderr, "File read failed: %s\n", strerror(errno));
			exit(1);
		}
		else if (n != req_len) {
			fprintf(stderr, "Only read %d of %d bytes from file\n",
					n, req_len);
			exit(1);
		}
	}
	else if (memread)
		memread_memory(req_addr, real_io + offset, req_len, iosize);
	else
		write_memory(real_io + offset, req_len, iosize, req_value);

	if (filename)
		close(ffd);
	close (mfd);

	return 0;
}

