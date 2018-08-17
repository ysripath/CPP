#include <iostream>
#include <climits>

using namespace std;
unsigned long fact(int n)
{
	if (n == 0)
		return 1;
	if (n == 1)
		return 1;

	return (n*fact(n-1));

}

int main()
{

	cout<<"Enter positive integer\n";
	int  N;
	cin>>N;
	if (N < 0)
	{
		cout<<"Invalid number\n";
		return 0;
	}
	unsigned long temp = fact(N);
	if (temp <=0
		|| temp > ULONG_MAX)
	{
		cout<<"Input number factorial is too large\n";
		return 0;
	}
	cout<<temp<<endl<<endl;
	return 0;
}
