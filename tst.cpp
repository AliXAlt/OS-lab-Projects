#include <iostream>
#include <thread>
using namespace std;

int count=1;

int inc()
{
    for (int i=0;i<100;i++){
        cout<<count<<endl;
        count ++;

    }
    return 0;
}


int main()
{
    
    thread T1(inc);
    thread T2(inc);
    cin.get();

    return 0;
}