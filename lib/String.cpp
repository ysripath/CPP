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

String::~String()
{
	if (buf != nullptr) {
		delete buf;
		buf = nullptr;
	}
}


String String::strrev(const String &arg)
{
	if (arg.length() == 0)
	{
		return String();
	}
	int l = arg.length();
	char* temp = new char[l];
	int k = 0;
	char* copy = new char[l];
	strcpy(copy, arg.getBuffer());
	//copy = arg.getBuffer();
	for (int i = l-1; i >= 0 ; i--) {
		temp[k++] = copy[i];
	}
	String copyStr(temp);
	return copyStr;
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


String& String::operator= (const String& str)
{
	  int l = str.length();
	  if (l > 0)
	  {
		  buf = new char[l];
		  strcpy(buf,str.getBuffer());
		  emptyFlag = false;
		  bufLength = l;
	  }
	  else
	  {
		  buf = nullptr;
		  bufLength = 0;
		  emptyFlag = true;
	  }
	  return *this;
}
