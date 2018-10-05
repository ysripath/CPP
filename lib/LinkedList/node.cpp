#include "node.h"

node::node()
{
	data = 0;
	next = nullptr;
}

node::node(T val)
{
	data = val;
	next = nullptr;
}

node::~node()
{
	if (next != nullptr)
		delete next;
	next = nullptr;
}

T node::getData()
{
	return data;
}

void node::setData(T val)
{
	data = val;
}
