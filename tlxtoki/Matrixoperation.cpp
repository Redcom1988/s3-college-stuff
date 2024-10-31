#include <iostream>
#include <vector>
using namespace std;

void printMatrix(const vector<vector<int>>& matrix) {
    for (const auto& row : matrix) {
        for (int val : row) {
            cout << val << " ";
        }
        cout << endl;
    }
}

void reflectHorizontal(vector<vector<int>>& matrix) {
    int N = matrix.size();
    int M = matrix[0].size();
    for (int i = 0; i < N / 2; ++i) {
        swap(matrix[i], matrix[N - 1 - i]);
    }
}

void reflectVertical(vector<vector<int>>& matrix) {
    int N = matrix.size();
    int M = matrix[0].size();
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M / 2; ++j) {
            swap(matrix[i][j], matrix[i][M - 1 - j]);
        }
    }
}

vector<vector<int>> rotate90(const vector<vector<int>>& matrix) {
    int N = matrix.size();
    int M = matrix[0].size();
    vector<vector<int>> rotated(M, vector<int>(N));
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            rotated[j][N - 1 - i] = matrix[i][j];
        }
    }
    return rotated;
}

vector<vector<int>> rotate180(const vector<vector<int>>& matrix) {
    return rotate90(rotate90(matrix));
}

vector<vector<int>> rotate270(const vector<vector<int>>& matrix) {
    return rotate90(rotate90(rotate90(matrix)));
}

int main() {
    int N, M, X;
    cin >> N >> M >> X;

    vector<vector<int>> matrix(N, vector<int>(M));
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            cin >> matrix[i][j];
        }
    }

    for (int i = 0; i < X; ++i) {
        string operation;
        cin >> operation;

        if (operation == "_") {
            reflectHorizontal(matrix);
        } else if (operation == "|") {
            reflectVertical(matrix);
        } else if (operation == "90") {
            matrix = rotate90(matrix);
        } else if (operation == "180") {
            matrix = rotate180(matrix);
        } else if (operation == "270") {
            matrix = rotate270(matrix);
        }
    }

    printMatrix(matrix);

    return 0;
}
