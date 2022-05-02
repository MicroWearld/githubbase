#include<stdio.h>
int Try_again(void);

int main() {
	char s[100],ch[100];
	int a[100],x=0,y=0;
	printf("Input:");
	scanf("%s",s);
	printf("0");
	while(s[x]!='\0') {
		while(s[x]>0) {
			a[y]=s[x]%2;
			s[x]=s[x]/2;
			y++;
		}
		for(y;y>0;y--)
			printf("%d",a[y-1]);
		printf("0");
		x++;
	}
	x=0;
    Try_again();
	return 0;
}

int Try_again() {
	int k;
	printf("\nTry again? Y=1/N=0:");
	scanf("%d",&k);
	if(k==1)
		main();
	else
		return 0;
}