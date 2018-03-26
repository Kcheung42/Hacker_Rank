#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    char* time = (char *)malloc(10240 * sizeof(char));
    scanf("%s",time);
	char **array;
	int	hours;
	int	minutes;
	int	seconds;

	array = (char **)malloc(sizeof(char *) * 3);
	array[0] = strtok(time, ":");
	hours = atoi(array[0]);
	array[1] = strtok(NULL, ":");
	minutes = atoi(array[1]);
	printf("here\n");
	if (strchr(array[2], 'P'))
	{
		array[2] = strtok(NULL, "P");
		hours = 24 - (12 - hours);
	}
	else
		array[2] = strtok(NULL, "A");
	seconds = atoi(array[2]);
	printf("%02d:%02d:%02d\n", hours, minutes, seconds);
    return 0;
}
