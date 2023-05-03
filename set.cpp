#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<pair<int,int>> generate_combinations(vector<int>& arr) {
    vector<pair<int,int>> combinations;
    int n = arr.size();
    int idx = 0;
    generate_n(back_inserter(combinations), n*(n-1)/2, [&](){
        int i = idx / (n-1);
        int j = idx % (n-1) + (idx % (n-1) >= i);
        idx++;
        return make_pair(arr[i], arr[j]);
    });
    return combinations;
}

int main() {
    vector<int> arr = {1, 2, 3, 4};
    vector<pair<int,int>> combinations = generate_combinations(arr);
    for (auto p : combinations) {
        cout << "[" << p.first << "," << p.second << "]" << endl;
    }
    return 0;
}
