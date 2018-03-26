#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int n; 
    scanf("%d",&n);

	char	*str;
	char	*str2;
	
	str = strnew(1);
	str[0] = '#';
	str2 = "#";
	while (n)
	{
		printf("%*s\n", n, str);
		str = realloc(str, strlen(str) + 1);
		str = strcat(str,str2);
		n--;
	}
    return 0;
}
