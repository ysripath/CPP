#include <bits/stdc++.h>
#include "Heap.h"
using namespace std;

int main()
{
	Heap h;
	while (true)
	{
		cout << "\nChoose Option\n";
		cout << " 1. Add		2. Peek			3.Poll		4.Traverse		5.Exit\n";
		int choice;
		cin >> choice;
		cout << "\n\n";
		switch (choice)
		{
		case 1: {
			int temp;
			cin >> temp;
			h.add(temp);
		} break;
		case 2: {
			cout << h.peek() << "\n";
		} break;
		case 3: {
			cout << "Polled for min " << h.poll() << "\n";
		} break;

		case 4: {
			h.printHeap();
		} break;
		default:
			return 0;
		}

	}
	
	return 0;
}