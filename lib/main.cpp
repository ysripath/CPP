#include <iostream>
#include "String.h"

using namespace std;

void testOutput();

void testCompare();

void testConcatenate();

void testSubStr();

void testCopy();

void testInput();
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

	testOutput();

	testCompare();

	testConcatenate();

	testSubStr();

	testCopy();

	testInput();
	return 0;
}

void testInput()
{
	String str_1;
	cout<<"Enter string content\n";
	cin>>str_1;
	cout<<str_1<<endl;
}


void testOutput()
{
	String str_1("Output str");
	cout<<str_1<<endl;
}

void testSubStr()
{
	String str_1("Hello");

	String str_2 = str_1.substr(2,2);

	cout<<"Sub string is "<<str_2.getBuffer()<<endl;

	String str_3 = str_2.substr(3,3);
	if (str_3.isEmpty())
		cout<<"Sub string is empty"<<endl;
	else
		cout<<"Sub string is "<<str_3.getBuffer()<<endl;

	String str_4 = str_1.substr(1,123);
	if (str_4.isEmpty())
		cout<<"Sub string is empty"<<endl;
	else
		cout<<"Sub string is "<<str_4<<endl;
}

void testConcatenate()
{
	String str_1("Hello");
	String str_2(" World");
	cout<<"Str_1 "<<str_1.getBuffer()<<endl;
	cout<<"Str_2 "<<str_2.getBuffer()<<endl;
	str_1 = str_1 + str_2;
	cout<<"Concatenated string is "<<str_1.getBuffer()<<endl;


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

void testCopy()
{
	String str_1("Test copy");
	char* buffer = nullptr;

	int ret = str_1.copy(&buffer, 5, 4);
	if (ret > 0)
		cout<<buffer<<endl;
	else
		cout<<"no characters werer copied"<<endl;

	delete[] buffer;
	buffer = nullptr;

	ret = str_1.copy(&buffer, 20, 4);
	if (ret > 0)
		cout<<buffer<<endl;
	else
		cout<<"no characters werer copied"<<endl;

	delete[] buffer;
	buffer = nullptr;

	ret = str_1.copy(&buffer, 1, 25);
	if (ret > 0)
		cout<<buffer<<endl;
	else
		cout<<"no characters werer copied"<<endl;

	delete[] buffer;
	buffer = nullptr;


}
