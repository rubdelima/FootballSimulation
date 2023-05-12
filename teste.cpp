#include<iostream>
#include<vector>
using namespace std;

vector<vector<int>> matrix = {
    {1,2,3,4,5,6,7}, {10, 20, 30, 40, 50, 60, 70}
};

int main(int argc, const char** argv) {
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[i].size(); j++) {
            cout << matrix[i][j]*10 << endl;
        }
    }
    return 0;
}
