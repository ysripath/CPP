// Linked List node

#pragma once

template<class T>
class node
{
public:
	T data; // Make it private
	node* next; // Mkae it private

	node();
	node(T val);
	~node();
	T getData();
	void setData(T val);
};

