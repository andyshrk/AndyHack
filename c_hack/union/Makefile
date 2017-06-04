CC = gcc
SRC = $(wildcard *.c)
OBJ = $(SRC:.c=.o)
TARGET = un
$(TARGET) : $(OBJ)
	@echo SRC: $(SRC)
	@echo OBJ: $(OBJ)
	$(CC) -o  $@ $(OBJ)
clean:
	rm -rf *.o $(TARGET)
.PHONY : clean
