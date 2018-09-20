// String library implementation file
#include "String.h"


String::String()
{
	buf = nullptr;
	bufLength = 0;
	emptyFlag = true;
}
String::String(const char  *arg)
{
	// Find the length of the argument and allocate memory accordinjgly
	int l = 0;
	const char* tempPtr = arg;
	while(*tempPtr){
		l++;
		tempPtr++;
	}
	if (l>0)
	{
		bufLength = l;
		buf = new char[l];
		strcpy(buf, arg);
		emptyFlag = true;
	}
	else
	{
		buf = nullptr;
		bufLength = 0;
		emptyFlag = false;
	}
}

String::String(const String &arg)
{
	const int l = arg.length();
	if (l >0)
	{
		int l = arg.length();
		buf = new char[l];
		strcpy(buf, arg.getBuffer());
		bufLength = arg.length();
		emptyFlag = true;
	}
	else
	{
		buf = nullptr;
		bufLength = 0;
		emptyFlag = false;
	}
}

char* String::getBuffer() const
{
	return buf;
}

int String::length() const
{
	return bufLength;
}

bool String::isEmpty() const
{
	return emptyFlag;
}
