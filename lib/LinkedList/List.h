// Custom Linked List class

#pragma once
#include <iostream>
#include "node.h"

template<class T>
class List
{
private:
	node<T>* head;
	node<T>* tail;
public:
	List();
	~List();
	void insertBack(T data);
	void insertFront(T data);
	void insertAtPos(T data, int pos);
	T getBack();
	T getFront();
	void deleteBack();
	void deleteFront();
	void clearList();
	void displayList();
	void reverseList();
	friend node<T>* reverseUtil(List<T>* l,node<T>* n);
};
