#include <iostream>
#include "String.h"

using namespace std;



void testCompare();

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
	String* revStr;// = nullptr;
	String str_1("Hello World");
	String::strrev(str_1, &revStr);
	cout<<"Given string is "<<str_1.getBuffer()<<endl;
	cout<<"Reverse string is "<<revStr->getBuffer() <<endl;
	delete revStr;
	revStr = nullptr;

	testCompare();

	return 0;
}


void testCompare()
{
	// Test for String compare
	String str_1("Hello World");
	String str_2("Hello World");
	if (!String::compare(str_1, str_2))
		cout<<"Duplicate strings"<<endl;
	else
		cout<<"Different strings"<<endl;

	String str_3("Hello world");
	if (!String::compare(str_1, str_3))
		cout<<"Duplicate strings"<<endl;
	else {
		cout<<str_1.getBuffer()<<"\t"<<str_3.getBuffer()<<endl;
		cout<<"Different strings - "<<String::compare(str_1, str_3)<<endl;
	}
}
