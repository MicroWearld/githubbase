#include <iostream>

using std::cout;
using std::endl;

void arr_change(int pos_from, int pos_to);
void b_sort(int arr);
void show_arr();
int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};

void show_arr() {
  int *p = arr;
  for (; p <= &arr[8]; p++) {
    cout << *p;
  }
  cout << endl;
}

void arr_change(int pos_from, int pos_to) {
  int i, tmp;
  if (pos_from > pos_to) {
    tmp = pos_to;
    pos_to = pos_from;
    pos_from = tmp;
  }
  tmp = arr[pos_from];
  for (i = pos_from + 1; i <= pos_to; i++) {
    arr[i - 1] = arr[i];
  }
  arr[pos_to] = tmp;
}

int main() {
  cout << "Origin: ";
  show_arr();
  arr_change(0, 8);
  cout << "Now: ";
  show_arr();
  return 0;
}
