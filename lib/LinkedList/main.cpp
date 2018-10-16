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
			cout<<"Enter data and position to be inserted in \n";
			int data;
			int pos;
			cin>>data>>pos;
			list->insertAtPos(data, pos);

		} break;
		case 4: {
			list->deleteFront();

		} break;
		case 5: {
			list->deleteBack();

		} break;
		case 6: {
			list->clearList();

		} break;
		case 7: {
			list->displayList();
		} break;
		default: break;
		}
	}
}
