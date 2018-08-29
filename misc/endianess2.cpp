#include <iostream>


using namespace std;


int main() 
{

	 int x = 1;
	char c;

	if (*(char*)&x ==1)
		cout<<"Little Endian\n";
	else
		cout<<"Big endian\n";


return 0;
}
