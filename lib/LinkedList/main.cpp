#include <iostream>
#include "List.h"

int main()
{
	List* list = new List();

	int choice;
	while()
	{
		cout<<"Enter operation: \n";
		cout<<"1. Insert at front  2. Insert at back  3. Insert at pos  4. Delete front\n" \
			  "5. Delete back  6. Clear List  7. Display List\n";
		cin>>choice;
		switch(choice)
		{
		case 1:
		case 2:
		case 3:
		case 4:
		case 5:
		case 6:
		case 7:
		default: break;
		}
	}
}
