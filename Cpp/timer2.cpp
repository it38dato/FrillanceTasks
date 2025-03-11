/*Пример с классом Counter, который представляет секундомер и хранит количество секунд*/
#include <iostream>
    using namespace std;
    class Counter{
    public:
        Counter(int sec){
            seconds = sec;
        }
        void display(){
            cout << seconds << " seconds" << endl;
        }
        Counter operator + (Counter c2){
            return Counter(this->seconds + c2.seconds);
        }
        int operator + (int s){
            return this->seconds + s;
        }
        int seconds;
    };
    int main(){
        Counter c1(20);
        Counter c2(10);
        Counter c3 = c1 + c2;
        c3.display();           // 30 seconds
        int seconds = c1 + 25;  // 45
        cout << seconds << endl;
        return 0;
    }