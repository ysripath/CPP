#include <iostream>

using namespace std;
int n;
void bubbleSort(int arr[]) {

	int i = 0;
	int j = i+1;
	for (int k = 0; k < n-1; k++) {
	j = k+1;
	
	while ( j < n) {
	
		if (arr[k] > arr[j]) {
			int temp = arr[j];
			arr[j] = arr[k];
			arr[k] = temp;
		}
		j++;
	}
	}

}


int main()
{
	cout<<"Enter number of numbers\n";
	
	cin>>n;
	
	int arr[10000];
	cout<<"Enter numbers\n";
	for (int i = 0; i < n; i++) {
		cin>>arr[i];
	}
	
	bubbleSort(arr);
	
	for(int i = 0; i < n; i++) {
		cout<<arr[i]<<"\t";
	}



return 0;
}
