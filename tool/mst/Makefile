CC = aarch64-linux-gnu-gcc
SRC = $(wildcard *.c)
OBJ = $(SRC:.c=.o)
TARGET = mst
$(TARGET) : $(OBJ)
	@echo SRC: $(SRC)
	@echo OBJ: $(OBJ)
	$(CC) -Os -o  $@ $(OBJ)
clean:
	rm -rf *.o $(TARGET)
.PHONY : clean
