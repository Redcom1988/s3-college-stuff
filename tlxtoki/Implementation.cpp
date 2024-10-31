#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

int main() {
    int rows, cols;
    cin >> cols >> rows; 

    int rotatedArr[rows][cols];

    for (int i = 0; i < cols; ++i) {
        for (int j = 0; j < rows; ++j) {
            cin >> rotatedArr[rows - 1 - j][i];
        }
    }

    for (int i = rows-1; i >= 0; --i) {
        for (int j = cols-1; j >= 0; j--) {
            cout << rotatedArr[i][j];
            if (j >= 0) cout << " ";
        }
        cout << endl;
    }

    return 0;
}