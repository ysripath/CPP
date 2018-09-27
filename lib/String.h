// String library header

#pragma once
#include <iostream>
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
	String substr(int pos, int len);
	int copy(char** buffer, int pos, int len);

	int length() const;
	char* getBuffer() const;
	bool isEmpty() const;

	// Operator overload
	String& operator = (const String &rhs);
	String& operator + (const String &rhs);
	friend std::istream& operator >>(std::istream &is, String &str);

};
std::ostream& operator <<(std::ostream &os, const String &str);

