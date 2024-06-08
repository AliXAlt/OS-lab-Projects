#include <iostream>
#include <vector>
#include <thread>
#include <random>
#include <algorithm>

using namespace std;


void quicksort(vector<int> &arr, int left, int right)
{
    if (left >= right)
    {
        return;
    }

    int mid = arr[(left + right) / 2];
    int i = left;
    int j = right;

    while (i <= j)
    {
        while (arr[i] < mid)
        {
            i++;
        }
        while (arr[j] > mid)
        {
            j--;
        }
        if (i <= j)
        {
            swap(arr[i], arr[j]);
            i++;
            j--;
        }
    }

    thread t1(quicksort, ref(arr), left, j);
    thread t2(quicksort, ref(arr), i, right);
    t1.join();
    t2.join();
};

int main()
{
    vector<int> arr(1000);
    int n = arr.size();
    
    for(int i=1; i<n; ++i) {
        arr[i] = i + 1;
    }
    
    random_device rd;
    mt19937 gen(rd());
    shuffle(arr.begin(),arr.end(),gen);
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;    
    quicksort(arr, 0, n - 1);
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
    return 0;
}
