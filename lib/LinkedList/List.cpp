// Custom Linked List class implementation

#include "List.h"
#include <iostream>
using namespace std;

template <class T>
List<T>::List()
{
	head = nullptr;
	tail = nullptr;
}


template <class T>
void List<T>::insertFront(T data)
{
	if (head == nullptr)
	{
		head = new node<T>(data);
		tail = head;
		return;
	}
	else
	{
		node<T>* tempNode = new node<T>(data);
		tempNode->next = head;
		head = tempNode;
	}
}


template <class T>
void List<T>::insertBack(T data)
{
	if (head == nullptr)
	{
		head = new node<T>(data);
		tail = head;
	}
	else
	{
		tail->next = new node<T>(data);
		tail = tail->next;
	}
}


template <class T>
T List<T>::getBack()
{
	if (tail != nullptr)
		return tail->data;
	else
		return NULL;
}

template <class T>
T List<T>::getFront()
{
	if (head != nullptr)
	{
		return head->data;
	}
	else
		return NULL;
}


template <class T>
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
		node<T>* temp = head;
		node<T>* cur = head;
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


template <class T>
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
		node<T>* temp = head;
		head = head->next;
		delete temp;
		temp = nullptr;
	}

}


template <class T>
void List<T>::clearList()
{
	if (head == nullptr)
		return;
	node<T>* temp = head;
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


template <class T>
void List<T>::displayList()
{
	cout<<"List contents\n";
	node<T> *temp = head;
	while (temp)
	{
		cout<<temp->getData()<< " ";
		temp = temp->next;
	}
	cout<<endl;
}
