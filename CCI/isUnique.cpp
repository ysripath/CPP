#include <iostream>

using namespace std;


bool unique(string str)
{
	int l = str.length();

	int checker = 0;
	for (int i  = 0; i < l; i++)
	{
		if ((checker & (1<<(int)(str[i]-'a'))) > 0)
			return false;
		else
			checker = checker | (1<<(int)(str[i]-'a'));
	}
	return true;
}	

int main()
{
	cout<<"Enter string\n";
	string str;
	cin>>str;
	if (unique(str))
		cout<<"Is unique\n";
	else
		cout<<"Not unique\n";
}
