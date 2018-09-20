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
	~String();
	static String strrev(const String &arg); // Returns the reverse of the given string

	int length() const;
	char* getBuffer() const;
	bool isEmpty() const;

	// Operator overload
	String& operator=(const String &rhs);
};
