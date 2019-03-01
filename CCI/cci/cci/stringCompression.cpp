#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>


using namespace std;


int compress(vector<char>& chars) {
	if (chars.size() == 0)
		return 0;
	if (chars.size() == 1)
		return 1;


	std::sort(chars.begin(), chars.end());

	int l = chars.size();
	int i = 0;
	int count = 1;
	int k = i;
	while (i < l - 1)
	{
		if (chars[i] == chars[i + 1])
		{
			count = 1;
			int j = i + 1;
			while (j < l)
			{
				if (chars[i] == chars[j])
				{
					count++;
					j++;
				}
				else
					break;
			}
			j--;
			if (count > 9)
			{
				char buf[100];
				sprintf(buf, "%d", count);
				int i = 0;
				while (buf[i] != '\0')
				{
					chars[++k] = buf[i];
					i++;
				}
				k++;
			}
			else {
				chars[++k] = '0' + count;
				k++;
			}
			//k = i+1;
			i = j;
			//k+=2;
			continue;
		}
		else
		{
			chars[k++] = chars[i++];
		}
	}
	k--;
	if (count > 1)
		chars.erase(chars.begin() + k + 1, chars.end());
	return chars.size();

}
int main()
{
	vector<char> v {'a','a','a','b','b','a','a'};
	int ret = compress(v);
	for (auto x : v)
		cout << x << " ";
	cout << "\n" << ret << "\n";
}