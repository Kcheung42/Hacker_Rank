#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int	calc_hourglass(int x, int y, int arr[])
{
	int sum;

	sum = 0;
	sum = arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x+1][y+2] + arr[x+2][y] + arr[x+2][y+1] + arr[x+2][y+2];
	return (sum);
}
int main(){
		int max_sum;
		int cur_sum;
	    int arr[6][6];
		max_sum = 0;
		cur_sum = 0;
		for(int arr_i = 0; arr_i < 6; arr_i++){
			for(int arr_j = 0; arr_j < 6; arr_j++){
				scanf("%d",&arr[arr_i][arr_j]);
			}
		}
		for (int j = 0; j < 4; j++) {
			for (int i = 0; i <  4; i++) {
				cur_sum = calc_hourglass(j,i,arr);
				if (cur_sum > max_sum)
				{
					max_sum = cur_sum;
				}
			}
		}
		printf("%d\n", max_sum);
		    return 0;
}
