#include <iostream>
#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;


int main()
{
	vector<int>	v;
	int N;
	cout<<"Enter number of elements\n";
	cin>>N;
	cout<<"Enter elements\n";
	for (int i = 0; i < N; i++)
		{
			int temp;
			cin>>temp;
			v.push_back(temp);
		}

	struct {
        bool operator()(int a, int b) const
        {   
		/*bool flag =  false;
		if (a == b)
			return a;
            //return a < b;
		int msb = 0;
		string aStr = to_string(a);
		string bStr = to_string(b);
		int size = ((aStr.length() < bStr.length())?aStr.length(): bStr.length());
		int i = 0;
		int lA = aStr.length();
		int lB = bStr.length();

		for (i = 0; i < size; i++)
		{
			int tempA = (int)(aStr[i]) - '0';
			int tempB = (int)(bStr[i]) - '0';
			if (tempA > tempB)
				return a;
			else if (tempB > tempA)
				return b;
			else if (tempA == tempB)
			{
				if (!flag) {
					msb = tempA;
					flag = true;
				}
				continue;
			}
		}
		i--;
		int tempVal;
		if (lA < lB)
		{
			tempVal = ((int)bStr[i+1] - '0');
			if (tempVal >= msb)
				return a;
			else
				return b; 
		}
		else //if  (aStr.length() > bStr.length())
		{
			tempVal = ((int)aStr[i+1] - '0');
			if (tempVal >= msb)
				return b;
			else
				return a;
		}*/
		if (a == b)
			return a;

		string strA = to_string(a);
		string strB = to_string(b);
		string strAB = strA + strB;
		string strBA = strB + strA;

		int A = stoi(strAB);
		int B = stoi(strBA);
		if (A>B)
			return a;
		else
			return b;
        }   
    } customLess;
	sort(v.begin(), v.end(), customLess);
	for (auto &a : v)
		cout<<a<<endl;
}
