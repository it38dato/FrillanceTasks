#include <iostream>
using namespace std;
int main() {
    char xo[3][3] = {
        {'.', '.','.'},
        {'.', '.','.'},
        {'.', '.','.'}
    };
    while(true) {
        int x, y;
        cin >> x >> y;
        xo[x][y] = 'x';
        for(int i=0;i<3; i++) {
            for(int j=0;j<3; j++) {
                cout << xo[i][j] << " ";
            }
            cout << endl;
        }
    }
    return 0;
}