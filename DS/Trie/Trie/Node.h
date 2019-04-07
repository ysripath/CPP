#pragma once
#include <iostream>
#include <vector>
class Node
{
public:
	int value;
	char ch;
	std::vector<Node*> *arr;

	Node()
	{
		value = INT_MIN;
		ch = '\0';
		arr = new std::vector<Node*>(26);
		for (auto &itr : *arr)
		{
			itr = NULL;
		}
	}

	void insert(char a)
	{
		value = INT_MIN;
		ch = a;
		int index = a - 'a';
		(*arr)[index] = new Node();
	}
	~Node()
	{
		arr->clear();
		delete arr;
	}
};