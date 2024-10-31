#include <bits/stdc++.h>
#include <vector>

using namespace std;

void quicksort(std::vector<int>& arr, int low, int high) {
    if (low < high) {
        int pivot = arr[high];
        int i = low - 1;

        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                swap(arr[i], arr[j]);
            }
        }
        swap(arr[i + 1], arr[high]);

        int pivotIndex = i + 1;
        quicksort(arr, low, pivotIndex - 1);
        quicksort(arr, pivotIndex + 1, high);
    }
}

int main() {
    int n;
    vector<int> arr[n];
    
    cin >> n;
    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;
        arr.push_back(num);
    }

    quicksort(arr, 0, arr.size() - 1);

    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}