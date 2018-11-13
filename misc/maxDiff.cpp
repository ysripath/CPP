#include <iostream>

using namespace std;

int arr[10];
int maxDiff()
{

	int max = -1;
	int i = 0;
	int j = 0;
	int small = 999999;
	int big = -1;

	small = arr[0];
	i = 0;
	j = i+1;
	while (i < 10 && j < 10)
	{
		if (arr[j] < small)
		{
			small = arr[j];
			i = j;
			j = i+1;
			continue;
		}
		else
		{
			int diff = arr[j] - small;
			max = (diff>max)?diff:max;
			j++;
			continue;
		}
	}
	return max;
	
}

int main()
{


cout<<"Enter array elements\n";
for (int i = 0; i < 10; i++)
	cin>>arr[i];

cout<<"Max diff is "<<maxDiff()<<endl;

}
