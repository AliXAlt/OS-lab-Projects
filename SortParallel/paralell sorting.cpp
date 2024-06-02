#include <iostream>
#include <vector>
#include <thread>

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
    vector<int> arr = {12, 54, 10, 65, 35, 77, 98, 5, 45};
    int n = arr.size();
    quicksort(arr, 0, n - 1);
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
    return 0;
}
