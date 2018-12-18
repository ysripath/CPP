#include <iostream>
#include <cstring>
using namespace std;


void swap(char *str, int i, int j)
{
        //std::swap(str[i], str[j]);
	char temp = str[i];
	str[i] = str[j];
	str[j] = temp;
}

void permute(char *str, int l, int r)
{
	if (l == r)
		cout<<str<<endl;
	else
	{
		for (int i = l; i <=r; i++)
		{
			swap(str, l, i);
			permute(str, l+1, r);
			swap(str, l, i);
		}
	}

}

int main()
{
	cout<<"Enter string\n";
	char str[100];
	cin.get(str, 100);
	int l = strlen(str);
	permute(str, 0, l-1);
	return 0;
}
