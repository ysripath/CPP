// Linked List node

#pragma once

template<class T>
class node
{
private:
	T data;
	node* next;
public:
	node();
	node(T val);
	~node();
	T getData();
	void setData(T val);
}

