#include <iostream>

using namespace std;

int main()

{
	char str[10000];
	cin>>str;
	cout<<str<<endl;
	char* p = "helloWorld";
	cout<<p<<endl;
	int l = 0;
	while (str[l] != '\0'){
		l++;
	}
	cout<<l<<endl;
	l = 0;
	while (*p) {
		l++;
		p++;
	}
	cout<<l<<endl;

	return 0;
}
