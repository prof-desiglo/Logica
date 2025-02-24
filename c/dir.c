#include <stdio.h>
#include <dirent.h>

int main(){
	struct dirent *dp;
	DIR *p_r = opendir("C:\\"); // O barra é um caracter especial no \n e o barra é \\
	while ( ( dp = readdir(p_r) ) != 0 ){
		printf("%s \n", (* dp).d_name);
	}
	return 0;
}
