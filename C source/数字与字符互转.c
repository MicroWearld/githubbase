#include<stdio.h>

int a,i;
char ch;
void Test(void);
int main()
{
	int a,i;
	char ch;
	printf("mod:\n");
	printf("1:number to letter 2:letter to number\n");
tar:printf("mod_choose:");
	scanf("%d",&i);
	if(i==1)
	{
		printf("input:");
		scanf("%d",&a);
		printf("output:%c\n",a);
	}
	else if(i==2)
	{
		Test();
	}
	printf("command:1:back 0:quit\n");
	printf("command_choose:");
	scanf("%d",&i);
	if(i==1)
	{
		putchar('\n');
		goto tar;
	}
	else
	return 0;
}

void Test()
{
	char cc;
	printf("Input:");
	scanf("%c",&cc);
	ch=getchar();
	printf("output:%d\n",ch);
}
