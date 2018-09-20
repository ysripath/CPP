#include <iostream>
#include "String.h"

using namespace std;

int main()
{
	cout<<"HELLO WORLD"<<endl;

	String str("test");
	cout<<"First string "<<str.getBuffer()<<endl;
	String str2;
	if (str2.isEmpty())
		cout<<"Empty String"<<endl;
	else
		cout<<"Not an empty string, contains - "<<str2.getBuffer()<<endl;
	return 0;
}
