#include <iostream>
#include "List.h"


using namespace std;
int main()
{
	List<int>* list = new List<int>();

	int choice;
	while(true)
	{
		cout<<"Enter operation: \n";
		cout<<"1. Insert at front  2. Insert at back  3. Insert at pos  4. Delete front\n" \
			  "5. Delete back  6. Clear List  7. Display List\n";
		cin>>choice;
		switch(choice)
		{
		case 1: {
			cout<<"Enter data\n";
			int data;
			cin>>data;
			list->insertFront(data);

		} break;
		case 2: {
			cout<<"Enter data\n";
			int data;
			cin>>data;
			list->insertBack(data);
		} break;
		case 3: {

		} break;
		case 4: {

		} break;
		case 5: {

		} break;
		case 6: {

		} break;
		case 7: {
			list->displayList();
		} break;
		default: break;
		}
	}
}
