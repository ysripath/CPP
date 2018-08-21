#include <iostream>

using namespace std;
int arr[10000];
int main()
{
cout<<"Enter size \n";
int N;
cin>>N;
int val1 = 0;
for (int i = 0; i < N; i++)
{

cin>>arr[i];
val1 ^= arr[i]; 
}

int val2 = 0;

for (int i = 1; i <=N+1; i++)
{
	val2 ^= i;
}
int v = val1^val2;
cout<<"Missing number is "<< v << endl;
return 0;
}
