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
	static void strrev(const String &arg, String **ptr); // Returns the reverse of the given string
	static int compare(const String &str1, const String &str2); // Compares if two Strings are same else return position of first mismatch

	int length() const;
	char* getBuffer() const;
	bool isEmpty() const;

	// Operator overload
	String& operator = (const String &rhs);
	String& operator + (const String &rhs);
};
