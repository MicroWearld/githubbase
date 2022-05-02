#include<stdio.h>
#include<math.h>
#define f(x) -2*x+8
#define F a-b

float k=0.1;
float a,b,c;
int Try_again(void);
void Test(void);
int main()
{
tar:printf("scan a,b,k \nInput:");
	scanf("%f,%f",&a,&b);
	do{
		c=(a+b)/2;
		printf("start:");
		Test();
		if(f(a)*f(c)<0)
		{
			b=c;
			printf("case1:");
			Test();
		}
		else if(f(c)==0)
		{
			a=c;
			printf("case2:");
			Test();
			break;
		}
		else
		{
			a=c;
			printf("case3:");
			Test();
		}
	}
	while(-F<=0.1&&F>=0.1);
	printf("Output:%f\n",a);
	if(Try_again()==1)
	goto tar;
	else
	return 0;
}

void Test()
{
	printf("a=%f,b=%f,c=%f,k=%f\n",a,b,k);
}

int Try_again()
{
	int k;
	printf("Try again? Y=1/N=0:");
	scanf("%d",&k);
	if(k==1)
	{
		putchar('\n');
		return 1;
	}
	else
	return 0;
}
