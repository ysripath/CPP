#include "Trie.h"
#include <iostream>
#include <string>
using namespace std;


int main()
{
	Trie* trieHandle = new Trie();
	while (true)
	{
		cout << "1. Insert         2. Find \n 3. Print All\n";
		int choice;
		cin >> choice;
		switch (choice)
		{
		case 1: {
			cout << "enter string\n";
			string str;
			cin >> str;
			trieHandle->insert(str);
		}
			break;
		case 2:{
			cout << "enter string\n";
			string str;
			cin >> str;
			if (trieHandle->find(str))
				cout << "Found\n";
			else
				cout << "Not Found\n";
		}
			break;
		case 3: {
			trieHandle->printAll();
		}
			break;
		default:
			return 0;
		}
	}
}