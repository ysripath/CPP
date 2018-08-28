#include <iostream>
#include <bitset>

using namespace std;


int main()
{
cout<<"Enter a number\n";
int n;
cin>>n;

bitset<sizeof(int)*8> foo(n);
cout<<foo<<endl;


int i = 0;

while (i < 32) {
n = n ^ (1<<i);

i++;
}

bitset<sizeof(int)*8> foo2(n);
cout<<foo2<<endl;

return 0;
}

