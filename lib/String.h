// String library header

#pragma once
#include <cstring>

class String {

private:
	char* buf;
	int bufLength;
	bool emptyFlag;

public:
	String();
	String(const char* arg);
	String(const String &arg);
	~String(){}
	int length() const;
	char* getBuffer() const;
	bool isEmpty() const;
};
