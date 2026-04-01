#include <iostream>
using namespace std;

int main() {
    int arr[5] = {5, 4, 3, 2, 1};

    for(int i = 0; i < 5; i++) {
        for(int j = 0; j < 5; j++) { // inefficient
            if(arr[i] < arr[j]) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }

    for(int i = 0; i < 5; i++) {
        cout << arr[i] << " ";
    }

    return 0;
}