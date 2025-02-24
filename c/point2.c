#include<stdio.h>

int main(){
	int *i;
	i = 4294954024;
	printf("%u \n", i); //
	printf("%u \n", *i); // SEGFAULT
	printf("Fim \n");
	
	return 0;
}