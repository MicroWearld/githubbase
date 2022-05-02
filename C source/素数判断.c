#include<stdio.h>

int Try_again(void);

int main() {
	int i,a,k;
	printf("input a number:");
	scanf("%d",&a);
	if(a<=1)
		printf("ERROR \n");
	else {
		for(i=2;i<a;i++) {
			if(a%i==0) {
				printf("i=%d \n",i);
				k=0;
			}
		}
		if(k!=0)
			printf("YES \n");
		else
			printf("NO \n");
	}
	printf("--------------------\n");
	Try_again();
	return 0;	
}

int Try_again() {
	int k;
	printf("Try again? Y=1/N=0:");
	scanf("%d",&k);
	if(k==1) {
		printf("--------------------\n");
		main();
	}
	else
		return 0;
}