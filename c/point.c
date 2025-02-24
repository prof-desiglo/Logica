#include<stdio.h>

int main(){
	int *i;
	int f = 2;
	printf("%u \n", f); // valor de F
	printf("%u \n", &f); // Endereço de F
	i = &f; // i Recebe o endereço de f
	printf("%u \n", i); // ???
	printf("%u \n", &i); // ???
	printf("%u \n", *i); // ???
	
	return 0;
}