/*For this letter of the English alphabet, you need to print the letter on the right on a standard keyboard. At the same time, the keyboard is closed, i.e. to the right of the letter «p» is the letter «a», from the letter «l» is the letter «z», and from the letter «m» — the letter
    Input: Первая строка входного файла INPUT.TXT содержит один символ — маленькую букву английского алфавита.
    Output: В выходной файл OUTPUT.TXT следует вывести букву стоящую справа от заданной буквы, с учетом замкнутости клавиатуры.*/
#include<iostream>
    #include<fstream>
    #include<cmath>
    using namespace std;
    ifstream in("input.txt");
    ofstream out("output.txt");
    int main()
    {
        const char massive=26;
        char a[massive]={
            'q','w','e','r','t','y','u','i','o','p','a',
            's','d','f','g','h','j','k','l','z','x','c',
            'v','b','n','m'
        };
        char symbol;
        in>>symbol;
        if(symbol=='m'){
            out<<a[0];
        }
        else{
            for(int i=0; i<massive; i++){
                if(symbol==a[i]){
                    out<<a[i+1];
                }

            }
        }
        return 0;
    }