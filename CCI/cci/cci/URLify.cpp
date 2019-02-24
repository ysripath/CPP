#include <bits/stdc++.h>

using namespace std;


void util(string& str)
{
	int l = str.length();
	l--;
	int i = l;
	while (i >= 0)
	{
		if (str[i] == ' ')
			i--;
		else
			break;
	}

	while (i >= 0)
	{
		if (str[i] != ' ')
		{
			str[l--] = str[i--];
			continue;
		}
		else
		{
			str[l--] = '0';
			str[l--] = '2';
			str[l--] = '%';
			i--;
			continue;
		}
	}
}


int main()
{
	//ios::sync_with_stdio(false);
	//cin.tie(NULL);
	cout << "Enter string \n";
	string str = "";
	char c;

	while (cin.get(c))
	{
		if (c == '\n')
			break;
		str += c;
	}
	util(str);
	cout << str << "\n";
	return 0;
}