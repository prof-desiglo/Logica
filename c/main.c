#include<stdio.h>
#include<gsl/gsl_math.h>

int main(){
	int x = gsl_fcmp(0.2,0.2, 0.01);
	printf("%d" , x);
	return 0;
}
