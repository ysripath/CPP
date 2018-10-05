// Custom Linked List class implementation

#include "List.h"

T List::head = nullptr;

List::List()
{
	head = nullptr;
	tail = nullptr;
}

void List::insertFront(T data)
{
	if (head == nullptr)
	{
		head = new node(data);
		tail = head;
		return;
	}
	else
	{
		node* tempNode = new node(data);
		tempNode->next = head;
		head = tempNode;
	}
}
