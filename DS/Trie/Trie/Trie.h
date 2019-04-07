#pragma once
#include <vector>
#include <algorithm>
#include <string>
#include <iostream>
#include <locale>
#include <iterator>

#include "Node.h"

class Trie
{
private:
	Node* head;

public:
	Trie();
	Trie(std::string word);
	void insert(std::string word, int value = INT_MIN);
	void remove(std::string word);
	bool find(std::string word);
	void printAll();
};


Trie::Trie()
{
	head = new Node();
}

Trie::Trie(std::string word)
{
	std::transform(word.begin(), word.end(), word.begin(), ::tolower);

	for (auto x : word)
	{
		if (!isalpha(x))
		{
			std::cout << "Error: Invalid English alphabet " << x << "\n";
			return;
		}
	}
	head = new Node();
	Node* cur = head;
	for (auto x : word)
	{
		if ((*cur->arr)[x - 'a'] != NULL)
			cur = (*cur->arr)[x - 'a'];
		else
		{
			cur->insert(x);
			cur = (*cur->arr)[x - 'a'];
		}
	}
}

void Trie::insert(std::string word, int value)
{
	Node* cur = head;
	std::transform(word.begin(), word.end(), word.begin(), ::tolower);
	
	for (auto x : word)
	{
		if (!isalpha(x))
		{
			std::cout << "Error: Invalid English alphabet "<<x<<"\n";
			return;
		}
	}

	for (auto x : word)
	{
		if ((*cur->arr)[x - 'a'] != NULL)
			cur = (*cur->arr)[x - 'a'];
		else
		{
			cur->insert(x);
			cur = (*cur->arr)[x - 'a'];
		}
	}
}

bool Trie::find(std::string word)
{
	std::transform(word.begin(), word.end(), word.begin(), ::tolower);

	for (auto x : word)
	{
		if (!isalpha(x))
		{
			std::cout << "Error: Invalid English alphabet " << x << "\n";
			return false;
		}
	}
	Node* cur = head;
	for (auto x : word)
	{
		if ((*cur->arr)[x - 'a'] != NULL)
			cur = (*cur->arr)[x - 'a'];
		else
		{
			return false;			
		}
	}
	return true;
}


void utilPrintAll(Node* node, std::string ret)
{
	if (node == NULL)
	{
		std::cout << "\n";
		return;
	}
	int index = 0;
	for (auto x : *(node->arr))
	{
		if (x != NULL)
		{
			//std::cout <<(char)( index + 'a');
			ret += (char)(index + 'a');
			utilPrintAll(x, ret);
			ret.pop_back();
		}
		index++;
	}
	std::cout<<ret << "\n";
}

void Trie::printAll()
{
	Node* cur = head;
	std::string ret = "";
	int index = 0;
	for (auto& x : *(cur->arr))
	{
		if (x != NULL)
		{
			//std::cout <<(char) (index + 'a');
			ret += (char)(index + 'a');
			utilPrintAll(x, ret);
			ret.pop_back();
			std::cout << "\n";
		}
		index++;
	}
	
}