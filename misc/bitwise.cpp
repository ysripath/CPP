#include <iostream>

using namespace std;
int main()
{


cout<<"Enter number\n";
int N;
cin>>N;

int choice;
while (true) {
	cout<<"1. Get bit 2. Set Bit  3. Flip bit  4. Clear bit \n";
	cin>>choice;
	int i;
	cout<<"Which bit?\n";
	cin>>i;
	switch(choice)
	{
		case 1:  {
				//cout<<"Which bit position? \n";

				//int i;
				//cin>>i;
				cout<< ((N>>i)&1) <<endl;
			}
			break;


		case 2: {
			N = (N|(1<<i));
			cout<<N<<endl;
			}
			break;


		case 3: {
			N = N^(1<<i);
			cout<<N<<endl;
			}
			break;

		case 4: {
			N = N & ~(1<<i);
			cout<<N<<endl;
			}
			break;
		default: return 0;

	} 
}


return 0;

}
