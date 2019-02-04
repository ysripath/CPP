#include "Heap.h"

Heap::Heap()
{
	capacity = 0;
	arr.emplace_back(-1); // Dummy value to deal with 1 to N indexing of the heap array
}

Heap::~Heap()
{
	arr.clear();
}

int Heap::getParentIndex(int index)
{
	int retVal = -1;
	try
	{
		retVal = index / 2;
		if (retVal < 1)
			throw;
	}
	catch (...)
	{
		cout << " Get parent of the root node \n";
		return -1;
	}

	return retVal;
}


int Heap::getLeftChildIndex(int index)
{
	int retVal = -1;

	if (index <= 0)
	{
		cout << "Invalid parent index\n";
		return -1;
	}

	retVal = index * 2;

	return retVal;
}

int Heap::getRightChildIndex(int index)
{
	int retVal = -1;

	if (index <= 0)
	{
		cout << "Invalid parent index\n";
		return -1;
	}

	retVal = (index * 2) + 1;
	return retVal;
}

bool Heap::hasLeft(int index)
{
	if (index <= 0)
	{
		cout << "Invalid parent index\n";
		return false;
	}

	if (index * 2 <= capacity)
		return true;
	else
		return false;
}

bool Heap::hasRight(int index)
{
	if (index <= 0)
	{
		cout << "Invalid Parent index\n";
		return false;
	}

	if ((index * 2) + 1 <= capacity)
		return true;
	else
		return false;
}

void Heap::swap(int i, int j)
{
	int temp = arr[i];
	arr[i] = arr[j];
	arr[j] = temp;
}

int Heap::peek()
{
	if (arr.size() <= 1)
	{
		cout << "Heap is empty\n";
		return -1;
	}

	return arr[1];
}

bool Heap::hasParent(int index)
{
	if ((index / 2) >= 1)
		return true;
	else
		return false;
}

void Heap::heapUp()
{
	int index = capacity; 
	while (hasParent(index))
	{
		int parentIndex = getParentIndex(index);
		if (arr[parentIndex] <= arr[index])
			return;
		else
		{
			swap(parentIndex, index);
			index = parentIndex;
		}
	}
	return;
}

void Heap::heapDown()
{
	int index = 1;
	
	while (index < capacity && hasLeft(index))
	{
		int leftIndex = getLeftChildIndex(index);
		int leftChildValue = arr[leftIndex];
		int rightChildValue = INT_MAX;
		int rightIndex = -1;
		int smallesIndex = leftIndex;
		int smallerValue = leftChildValue;

		if (hasRight(index))
		{
			rightIndex = getRightChildIndex(index);
			rightChildValue = arr[rightIndex];
			if (rightChildValue < smallerValue)
			{
				smallerValue = rightChildValue;
				smallesIndex = rightIndex;
			}
		}

		if (arr[index] <= leftChildValue && arr[index] <= rightChildValue)
			return;		
		swap(index, smallesIndex);
		index = smallesIndex;
	}	
}

void Heap::add(int val)
{
	capacity++;
	arr.emplace_back(val);
	heapUp();
}

int Heap::poll()
{

	if (arr.size() <= 1)
	{
		cout << "Empty heap\n";
		return -1;
	}
	int retVal = arr[1];
	int temp = arr[capacity];
	capacity--;
	arr.pop_back();
	arr[1] = temp;
	heapDown();
	return retVal;
}


void Heap::printHeap()
{
	if (arr.size() <= 1)
	{
		cout << "Empty heap\n";
		return;
	}

	queue<int> qIndex;
	qIndex.push(1);
	while (!qIndex.empty())
	{
		int numberOfLevelElements = qIndex.size();
		while (numberOfLevelElements > 0)
		{
			int index = qIndex.front();
			cout << arr[index] << "\t";
			qIndex.pop();
			if (hasLeft(index))
				qIndex.push(getLeftChildIndex(index));
			if (hasRight(index))
				qIndex.push(getRightChildIndex(index));
			numberOfLevelElements--;
		}
		cout << "\n";
	}
}