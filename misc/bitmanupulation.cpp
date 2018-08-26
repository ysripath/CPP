#include <iostream>
#include <string>
#include <bitset>


using namespace std;




void printBinaryFormat(int N)
{

	
	bitset<sizeof(int)*8> foo(N);
	cout<<foo<<endl;
}


bool checkAlternate(int N)
{
	int i = 0;
	int j = 1;

	while (N)
	{
		if (((N>>i)&1) == ((N>>j)&1))
			return false;
		
		N >>= 1;
	}
	return true;

}

int main()
{


cout<<"Enter number\n";
int N;
cin>>N;

cout<<"Binary representation \n";

printBinaryFormat(N);


if (checkAlternate(N))
	cout<<"Alternate bits\n";
else
	cout<<"Not alternate\n";

return 0;
}
