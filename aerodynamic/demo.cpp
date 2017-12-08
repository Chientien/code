#include<iostream>
#include<cmath>
using namespace std;

int f(float x)
{
    float r;
    r = x*2 + pow(x,3);
    return r;
}

int main()
{
    float r, x=1.2;
    r = f(x);
    cout<<r<<endl;
    cout<<"Hello, world."<<endl;
    return 0;
}
