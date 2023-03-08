#include <exception>
#include "BagIterator.h"
#include "Bag.h"

using namespace std;


BagIterator::BagIterator(const Bag& c): bag(c)
{
	if (this->bag.isEmpty())
	{
		//throw exception();
		this->amount = -1;
		this->position = -1;
	}
	else
	{
		this->amount = 0;
		this->position = 0;
		for (int i = 0; i < this->bag.range; i++)
			if (this->bag.data[i] != 0)
			{
				this->amount = this->bag.data[i];
				this->position = i;
				return;
			}
	}
}
//Best case: Theta(1)
//Worst case: Theta(range)
//Total complexity: O(range)


void BagIterator::first() {
	if (this->bag.isEmpty())
		throw exception();
	for (int i = 0; i < this->bag.range; i++)
		if (this->bag.data[i] != 0)
		{
			this->amount = this->bag.data[i];
			this->position = i;
			return;
		}
}
//Best case: Theta(1)
//Worst case: Theta(range)
//Total complexity: O(range)


void BagIterator::next() {
	if (this->position >= this->bag.range || this->position < 0)
		throw exception();
	this->amount--;
	if (this->amount == 0)
	{
		this->position++;
		while (this->position < this->bag.range)
		{
			if (this->bag.data[this->position] != 0)
			{
				this->amount = this->bag.data[this->position];
				return;
			}
			this->position++;
		}
	//throw exception();
	}
}
//Best case: Theta(1)
//Worst case: Theta(range)
//Total complexity: O(range)


bool BagIterator::valid() const {
	if (this->position < this->bag.range && this->amount > 0 && this->position >= 0)
		return true;
	return false;
}
//Theta(1)



TElem BagIterator::getCurrent() const
{
	if (this->position >= this->bag.range || this->amount <= 0 || this->position < 0)
		throw exception();

	return this->position + this->bag.lowerBound;
}
//Theta(1)
