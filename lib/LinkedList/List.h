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

	friend node<int>* reverseUtil(List<int>* l,node<int>* n);
	friend node<float>* reverseUtil(List<float>* l,node<float>* n);
	friend node<double>* reverseUtil(List<double>* l,node<double>* n);
};
