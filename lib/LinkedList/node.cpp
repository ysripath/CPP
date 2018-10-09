#include "node.h"

node<T>::node()
{
	data = 0;
	next = nullptr;
}

node<T>::node(T val)
{
	data = val;
	next = nullptr;
}

node<T>::~node()
{
	if (next != nullptr)
		delete next;
	next = nullptr;
}

T node<T>::getData()
{
	return data;
}

void node<T>::setData(T val)
{
	data = val;
}
