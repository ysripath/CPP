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
void List<T>::insertAtPos(T data, int pos)
{
	if (pos < 1)
	{
		cout<<"Invalid position\n";
	}
	else if (head == nullptr
			&& pos > 1)
	{
		cout <<"Invalid position \n";
	}

	else if (head == nullptr
			&& pos == 1)
	{
		head = new node<T>(data);
		tail = head;
	}
	else
	{
		int count = 0;
		node<T>* temp = head;
		while (temp)
		{
			count++;
			if (count == pos)
			{
				node<T>* cur = new node<T>(data);
				cur->next = temp->next;
				temp->next = cur;
				if (cur->next == nullptr)
				{
					tail = cur;
				}
				return;
			}
			else
			{
				temp = temp->next;
			}
		}
		if (++count == pos)
		{
			tail->next = new node<T>(data);
			tail = tail->next;
		}
	}
	return;
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
	else
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
		node<T>* temp = head->next;
		delete head;
		head = temp;
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


node<int>* reverseUtil(List<int>* l,node<int>* n)
{
	if (n->next == nullptr)
	{
		l->head = n;
		return l;
	}
	node<int>* tempNode = reverseUtil(l, n->next);
	tempNode->next = n;
	return n;
}

template <class T>
void List<T>::reverseList()
{
	if (head == nullptr && tail == nullptr)
	{
		cout<<"empty list\n";
		return;
	}
	tail = reverseUtil(this, head);
	displayList();
}
template class List<int>;
template class List<float>;
template class List<double>;

