#include "node.h"

template <class T>
node<T>::node()
{
	data = 0;
	next = nullptr;
}

template <class T>
node<T>::node(T val)
{
	data = val;
	next = nullptr;
}

template <class T>
node<T>::~node()
{
	next = nullptr;
}

template <class T>
T node<T>::getData()
{
	return data;
}

template <class T>
void node<T>::setData(T val)
{
	data = val;
}

template class node<int>;
template class node<float>;
template class node<double>;
