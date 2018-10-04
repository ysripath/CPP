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
		buf = new char[l+1];
		strcpy(buf, arg);
		emptyFlag = false;
	}
	else
	{
		buf = nullptr;
		bufLength = 0;
		emptyFlag = true;
	}
}

String::String(const String &arg)
{
	const int l = arg.length();
	if (l >0)
	{
		int l = arg.length();
		buf = new char[l+1];
		strcpy(buf, arg.getBuffer());
		bufLength = arg.length();
		emptyFlag = false;
	}
	else
	{
		buf = nullptr;
		bufLength = 0;
		emptyFlag = true;
	}
}

String::~String()
{
	if (buf != nullptr) {
		delete[] buf;
		buf = nullptr;
	}
}


String String::substr(int pos, int len)
{
	if (len <= 0)
		return String();

	if (pos >= bufLength)
		return String();
	if (len > bufLength)
	{
		len = bufLength - pos;
	}

	char* tempBuf = new char [len+1];
	int i = pos;
	int count = 0;
	while (count < len
		   && i < bufLength)
	{
		tempBuf[count++] = buf[i++];
	}
	tempBuf[count] = '\0';

	String str(tempBuf);

	delete[] tempBuf;
	tempBuf = nullptr;
	return str;
}

void String::strrev(const String &arg, String **ptr)
{
	if (arg.length() == 0)
	{
		ptr = nullptr;
		return;
	}
	int l = arg.length();
	char* temp = new char[l+1];
	memset(temp, 0,l+1 );
	int k = 0;
	char* copy = new char[l+1];
	strcpy(copy, arg.getBuffer());
	//copy = arg.getBuffer();
	for (int i = l-1; i >= 0 ; i--) {
		temp[k++] = copy[i];
	}
	*ptr = new String(temp);
	//String copyStr(temp);
	delete[] copy;
	copy = nullptr;
	delete[] temp;
	temp = nullptr;
	//return copyStr;
}



int String::compare(const String &str1, const String &str2)
{
	if (str1.length() == 0 && str2.length() == 0)
		return true;
	int l = (str1.length() < str2.length())?str1.length():str2.length();
	for (int i = 0; i < l; i++)
	{
		if (str1.buf[i] == str2.buf[i])
			continue;
		else
		{
			return i+1;
		}
	}
	if (str1.length() != str2.length())
		return l+1;
	else
		return 0;
}


int String::copy(char **buffer, int pos, int len)
{
	if (pos >= bufLength)
	{
		*buffer = nullptr;
		return 0;
	}

	if (len >= bufLength)
		len = bufLength;

	int tempL = bufLength -pos;
	*buffer = new char[tempL+1];
	memset(*buffer, 0, tempL+1);
	int k = pos;
	int count = 0;
	while (count < len
		   && k < bufLength) {
		(*buffer)[count] = buf[k];
		count++;
		k++;
	}
	(*buffer)[count] = '\0';
	return count+1;
}

int String::find_first_of(const char ch)
{
	if (emptyFlag)
		return -1;
	int l = bufLength;
	int i = 0;
	while (i < l)
	{
		if (buf[i] == ch)
			return i;
		i++;
	}
	return -1; // ch not found in String
}


int String::find_last_of(const char ch)
{
	if (emptyFlag)
		return -1;
	int l = bufLength;
	int i = l-1;
	while (i >= 0)
	{
		if (buf[i] == ch)
			return i;
		i--;
	}
	return -1; // ch not found in String
}


int String::find_n_of(const char ch)
{
	if (emptyFlag)
		return -1;
	int l = bufLength;
	int count = 0;
	int i = 0;

	while (i < l)
	{
		if (buf[i] == ch)
			count++;
		i++;
	}
	return count;
}

void String::clear()
{
	if (buf == nullptr)
		return;
	delete[] buf;
	buf = nullptr;
	bufLength = 0;
	emptyFlag = true;
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

String& String::operator + (const String& str)
{
	int l2 = str.length();
	if (l2 > 0)
	{
		int l1 = this->length();
		int totalLength = l1+l2;
		char* tempBuf = new char[totalLength+1];
		strcpy(tempBuf, this->getBuffer());
		strcat(tempBuf, str.getBuffer());
		delete[] this->buf;
		this->buf = new char[totalLength+1];
		strcpy(this->buf, tempBuf);
		delete[] tempBuf;
		tempBuf = nullptr;
		return *this;
	}
	else
	{
		return *this;
	}
}

String& String::operator = (const String& str)
{
	if (str.buf == this->buf)
		return *this;
	  int l = str.length();
	  if (l > 0)
	  {
		  buf = new char[l+1];
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

char& String::operator [] (const int &index)
{
	if (index > this->bufLength
			|| index < 0)
	{
		static char tempChar = '\0';
		return tempChar;
	}
	else
		return this->buf[index];
}


std::istream& operator >> (std::istream& is, String &str)
{
	char temp[100];
	is.get(temp, 100, '\n');
	String tempStr(temp);
	str = tempStr;
	return is;
}

std::ostream& operator << (std::ostream& os, const String &str)
{
	if (str.emptyFlag)
	{
		os << "";
	}
	else
	{
		os << str.getBuffer();
	}
	return os;
}

const char* String::c_str()
{
	return buf;
}
