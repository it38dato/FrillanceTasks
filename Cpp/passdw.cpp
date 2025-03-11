/*Функция ввода пароля.*/
#include <iostream>
    #include <string>
    using namespace std;
    void check_pass (string password){
        string valid_pass="qwerty123";
        if (password==valid_pass){
            cout<<"Доступ разрешен." << endl;
        } else {
            cout << "Неверный пароль!" << endl;
        }
    }
    int main()
    {
        setlocale(LC_CTYPE, "rus");
        string user_pass;
        cout<< "Введите пароль: ";
        getline(cin, user_pass);
        check_pass(user_pass);
        return 0;
    }