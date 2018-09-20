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

	// Check string reverse;
	String revStr;// = nullptr;
	String str_1("Hello World");
	revStr = String::strrev(str_1);
	cout<<"Given string is "<<str_1.getBuffer()<<endl;
	cout<<"Reverse string is "<<revStr.getBuffer()<<endl;

	return 0;
}
