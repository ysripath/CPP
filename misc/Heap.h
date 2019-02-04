#pragma once
#include <bits/stdc++.h>
using namespace std;
class Heap
{
public:
	Heap();
	~Heap();
	vector<int> arr;
	int capacity;
	int peek();
	int poll();
	void swap(int i, int j);
	bool hasLeft(int i);
	bool hasRight(int i);
	bool hasParent(int i);
	void heapUp();
	void heapDown();
	void add(int val);
	int getParentIndex(int i);
	int getLeftChildIndex(int i);
	int getRightChildIndex(int i);
	void printHeap();
};
