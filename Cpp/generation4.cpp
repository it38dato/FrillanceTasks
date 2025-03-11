/*Разработаем программу, в которой создадим одномерный динамический массив, заполненный случайными числами.*/
#include <iostream>
    #include <ctime>
    using namespace std;
    int main()
    {
        srand(time(0)); // генерация случайных чисел
            int *ptrarray = new int [10]; // создание динамического массива вещественных чисел на десять элементов
            for (int count = 0; count < 10; count++)
                    ptrarray[count] = (rand() % 10 + 1) / int((rand() % 10 + 1)); //заполнение массива случайными числами с масштабированием от 1 до 10
            cout << "array = ";
            for (int count = 0; count < 10; count++)
                    cout << ptrarray[count] << "    ";
            delete [] ptrarray; // высвобождение памяти
            cout << endl;
        return 0;
    }