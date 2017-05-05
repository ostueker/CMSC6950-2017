CC=gcc
CFLAGS=-I.
DEPS = hellomake.h
OBJ= hellomake.o hellofunc.o

hellomake: $(OBJ) 
	$(CC) -o  $@  $^  $(CFLAGS)

%.o: %.c $(DEPS)
	$(CC) -c -o  $@  $<  $(CFLAGS)

.PHONY: clean

clean:
	rm $(OBJ)
	rm hellomake
