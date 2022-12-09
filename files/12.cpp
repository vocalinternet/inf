#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <cstdlib>
#include <algorithm>
using namespace std;

int comp(const void *i, const void *j) { // функция, сортировка матрицы по возрастанию
  return *(int*) i - *(int*) j;
}

int funMas(int i, int j, int size) { // функция, для управления матрицей
  int line = 0;
  if (i >= 1) {
    line = ((i - 1) * size) + j - 1;
  }
  return line;
}

int main() {
  cout << "Matrix size, 2, 4, 6, 8: "; // ввод размера матрицы
  int size = 0;
  while (!(cin >> size and (size == 2 or size == 4 or size == 6 or size == 8))) { // проверка на допустимый размер
    cout  << "Incorrect matrix size! Matrix size, 2, 4, 6, 8: ";
    cin.clear();
    cin.ignore(32767, '\n');
  }

  int *Matrix = new int[size * size]; // создание матрицы (через указатель)
  int i = 1;
  int j = 1;
  
  cout << "Would you like to enter the numbers yourself? 1 - Yes, 2 - No: "; // выбор, вводить ли значения самостоятельно или автоматически
  int choice = 0;
  while (!(cin >> choice and (choice == 1 or choice == 2))) { // проверка на допустимый выбор
    cout << "Incorrect input! 1 - Yes, 2 - No: ";
    cin.clear();
    cin.ignore(32767, '\n');
  }

  if (choice == 1) { // ручной ввод значений
    for (int temp = 1; temp < (size * size + 1); temp++) { // ввод до заполнения матрицы
      cout << "Enter a number: ";
      while (!(cin >> Matrix[funMas(i, j, size)] and (Matrix[funMas(i, j, size)] > 0 and Matrix[funMas(i, j, size)] < 101))) { // проверка на допустимое значение
        cout << "Incorrect number! The number can be from 1 to 100: ";
        cin.clear();
        cin.ignore(32767, '\n');
      }
      j++;
      
      if (j == (size + 1)) { // переход на новую строчку
        j = 1;
        i++;
      }
    }
  }
  else if (choice == 2) { // автоматический ввод значений
      srand(time(NULL));
      for (int i = 1; i <= size; i++) {
          for (int j = 1; j <= size; j++) {
              Matrix[funMas(i, j, size)] = rand() % (0, 100) + 1; // ввод случайных чисел
          }
      }
  }

  for (int i = 1; i <= size; i++) { // вывод введённой матрицы на экран
    for (int j = 1; j <= size; j++) {
      cout << Matrix[funMas(i, j, size)] << "  ";
      }
    cout << endl;
  }
  
  cout << "-------------------" << endl;
  
  qsort(Matrix, (size * size), sizeof(int), comp); // сортировка матрицы по возрастанию
  int maxSize = size * size - 1;
  
  for (int minSize = 0; minSize != size * (size / 2); minSize++) { // сортировка по убыванию
    swap(Matrix[minSize], Matrix[maxSize - minSize]);
  }

  for (int i = 1; i <= size; i++) { // вывод отсортированной матрицы на экран
    for (int j = 1; j <= size; j++) {
      cout << Matrix[funMas(i, j, size)] << "  ";
      }
    cout << endl;
  }
}
