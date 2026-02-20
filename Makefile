CFLAGS = -Wall -Wextra -g -lraylib -lGL -lm -lpthread -ldl -lrt -lX11 
CC = gcc

all: 
	$(CC) main.c -o particle_simulation $(CFLAGS)

clean:
	rm -f main.o particle_simulation
