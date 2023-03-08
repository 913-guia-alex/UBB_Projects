
#include "Bag.h"
#include "BagIterator.h"

#include <exception>
#include <iostream>
#include <cmath>

using namespace std;


Bag::Bag() {
	this->data = new TElem(0);
	this->range = 0;
	this->lowerBound = NULL_TELEM;
	this->upperBound = NULL_TELEM;
}
//Theta(1)

bool Bag::resize(TElem lower, TElem upper)
{
	int newRange = (upper - lower) + 1;

	TElem* newData = new TElem[newRange];

	if (newData == NULL)
		return false;

	int index = 0;
	int newIndex;

	if (lower != this->lowerBound)
		newIndex = newRange - this->range;
	else 
		newIndex = 0;

	for (int i = 0; i < newRange; i++)
		newData[i] = 0;

	while (newIndex < newRange && index < this->range)
		newData[newIndex++] = this->data[index++];

	TElem* aux = this->data;

	this->data = newData;
	this->range = newRange;
	this->lowerBound = lower;
	this->upperBound = upper;

	delete[] aux;

	return true;
}
//Theta(range)

void Bag::add(TElem elem) {
	if (this->range == 0)
	{
		bool ok = this->resize(this->lowerBound, elem);
		if (!ok)
			return;

		this->lowerBound = elem;
		this->upperBound = elem;
		this->range = 1;
	}
	else if (elem < lowerBound)
	{
		bool ok = this->resize(elem, this->upperBound);
		if (!ok)
			return;
	}
	else if (elem > upperBound)
	{
		bool ok = this->resize(this->lowerBound, elem);
		if (!ok)
			return;
	}

	int position = abs(this->lowerBound - elem);
	this->data[position]++;
}
//Best case: theta(1)
//Worst case: theta(range)
//Total complexity: O(range)


bool Bag::remove(TElem elem) {
	if (elem < this->lowerBound || elem > this->upperBound)
		return false;

	int position = abs(this->lowerBound - elem);

	if (this->data[position] == 0)
		return false;
	else
		this->data[position]--;

	return true; 
}
//Theta(1)


bool Bag::search(TElem elem) const {
	if (elem < this->lowerBound || elem > this->upperBound)
		return false;

	int position = abs(this->lowerBound - elem);

	if (this->data[position] == 0)
		return false;

	return true;
}
//Theta(1)

int Bag::nrOccurrences(TElem elem) const {
	if (elem < this->lowerBound || elem > this->upperBound)
		return 0;

	int position = abs(this->lowerBound - elem);

	return this->data[position];
}
//Theta(1)


int Bag::size() const {
	int nr = 0;

	for (int i = 0; i < this->range; i++)
		nr += this->data[i];

	return nr;
}
//Theta(range)


bool Bag::isEmpty() const {
	int nr = 0;

	for (int i = 0; i < this->range; i++)
		nr += this->data[i];

	return (nr == 0);
}
//Theta(range)

int Bag::removeOccurrences(int nr, TElem elem)
{
	if (nr < 0)
		throw std::exception("Nr of occurences must be positive");
	if (elem < this->lowerBound || elem > this->upperBound)
		return 0;

	int position = abs(this->lowerBound - elem);

	if (this->data[position] < nr)
	{ 
		int nrOccurences = this->data[position];
		this->data[position] = 0;
		return nrOccurences;
	}

	return 0;
}
//Theta(1)

BagIterator Bag::iterator() const {
	return BagIterator(*this);
}
//Theta(1)


Bag::~Bag() {
	delete[] this->data;
}
//Theta(1)

