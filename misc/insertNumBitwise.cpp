#include <iostream>
#include <bitset>


using namespace std;
int main()
{

cout<<"Enter m, n, i , j values\n";
int M, N, i, j;
cin>>M>>N>>i>>j;
bitset<sizeof(int)*8> foo(M);
//cout<<M<<endl;

for (int x = i; x <= j; x++) {
	M = M & ~(1<<x);
}

//cout<<"After clearing bits\n";
bitset<sizeof(int)*8> foo2(M);
//cout<<foo2<<endl;

// Merge bits

for (int x = i; x <= j; x++) {
	int val = N&1;
	M = M ^ (val <<x);
	N = N>>1;
}

bitset<sizeof(int)*8> foo3(M);
cout<<foo3<<endl;


}
