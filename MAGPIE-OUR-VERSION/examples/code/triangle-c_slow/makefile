CC=/opt/rh/devtoolset-9/root/usr/bin/gcc

all: standalone run_triangle test_triangle

triangle.o: triangle.c
	$(CC) -c triangle.c -o triangle.o

standalone: standalone.c triangle.o
	$(CC) -o standalone standalone.c triangle.o

run_triangle: run_triangle.c triangle.o
	$(CC) -o run_triangle run_triangle.c triangle.o

test_triangle: test_triangle.c triangle.o
	$(CC) -o test_triangle test_triangle.c triangle.o

clean:
	rm -f standalone run_triangle test_triangle triangle.o
