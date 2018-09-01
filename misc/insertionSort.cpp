#include <iostream>

using namespace std;



void sort(int arr[], int n)
{

	for (int i = 1; i < n; i++)
	{
		int key = arr[i];
		int j = i-1;
		while (j >= 0 &&  arr[j] > key) {
			arr[j+1] = arr[j];
			j--;
		}
		arr[j+1] = key;
	}
}

int main() 
{


int arr[1000];

int n;
cout<<"Enter n\n";
cin>>n;
for (int i = 0; i < n; i++)
{

	cin>>arr[i];
}

sort(arr,n);

for (int i = 0; i < n; i++) 
{
	cout<<arr[i]<<" ";
}
cout<<endl;

return 0;
}
