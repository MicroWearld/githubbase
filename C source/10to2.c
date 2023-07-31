#include <stdio.h>
void p_line(void);
int Try_again(void);
int main() {
  int x, i;
  int a[100];
loop:
  printf("Input:");
  i = 0;
  scanf("%d", &x);
  // printf("Debug list");						//debug
  // mode code
  // p_line(); //debug mode code
  while (x > 0) {
    a[i] = x % 2;
    x = x / 2;
    // printf("i=%d,x=%d\n",i,x);			//debug mode code
    i++;
  }
  // putchar('\n'); //debug mode code
  printf("Output:"); // normal mod code
  for (i; i > 0; i--) {
    // printf("i=%d,a[i]=%d\n",i,a[i]);		//debug mode code
    printf("%d", a[i - 1]); // normal mod code
  }
  // printf("---------");						//debug
  // mode code
  // p_line(); //debug mode code
  if (Try_again() == 1) {
    putchar('\n');
    goto loop;
  } else
    return 0;
}

int Try_again() {
  int k;
  printf("\nTry again? Y=1/N=0:");
  scanf("%d", &k);
  if (k == 1)
    return 1;
  else
    return 0;
}

void p_line() {
  int k;
  for (k = 1; k <= 70; k++)
    putchar('-');
}
