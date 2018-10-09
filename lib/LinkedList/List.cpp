// Custom Linked List class implementation

#include "List.h"

T List::head = nullptr;

List<T>::List()
{
	head = nullptr;
	tail = nullptr;
}

void List<T>::insertFront(T data)
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


void List<T>::insertBack(T data)
{
	if (head == nullptr)
	{
		head = new node(data);
		tail = head;
	}
	else
	{
		tail->next = new node(data);
		tail = tail->next;
	}
}

T List<T>::getBack()
{
	if (tail != nullptr)
		return tail->data;
	else
		return NULL;
}

T List<T>::getFront()
{
	if (head != nullptr)
	{
		return head->data;
	}
	else
		return NULL;
}

void List<T>::deleteBack()
{
	if (head == nullptr)
		return;
	else if (head == tail)
	{
		delete tail;
		head = nullptr;
		tail = nullptr;
	}
	{
		node* temp = head;
		node* cur = head;
		while (temp->next)
		{
			cur = temp;
			temp = temp->next;
		}
		delete temp;
		temp = nullptr;
		cur->next = nullptr;
		tail = cur;
	}
}

void List<T>::deleteFront()
{
	if (head == nullptr)
		return;
	else if (head == tail)
	{
		delete head;
		head = nullptr;
		tail = nullptr;
	}
	else
	{
		node* temp = head;
		head = head->next;
		delete temp;
		temp = nullptr;
	}

}


void List<T>::clearList()
{
	if (head == nullptr)
		return;
	node* temp = head;
	while (head)
	{
		temp = head;
		head = head->next;
		delete temp;
		temp = nullptr;
	}
	head = nullptr;
	tail = nullptr;
}
