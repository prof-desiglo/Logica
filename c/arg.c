#include<stdio.h>
#include <stdlib.h>

int soma(int a, int b){
	return a + b;
}


int main(int argc, char *argv[]){
	if(argc != 3){
		printf("Menos de 2 argumentos");
		return -1;
	}
	
	printf("%s \n", argv[0]);
	
	int a = atoi(argv[1]);
	int b = atoi(argv[2]);

	int c = soma(a,b);
	printf("%d \n", c);
		
	return 0;
}
