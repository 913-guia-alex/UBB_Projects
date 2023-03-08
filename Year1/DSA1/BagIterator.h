#include "Bag.h"

class BagIterator
{
	//DO NOT CHANGE THIS PART
	friend class Bag;
	
private:
	const Bag& bag;
	int position;
	int amount;

	BagIterator(const Bag& c);
public:
	void first();
	void next();
	TElem getCurrent() const;
	bool valid() const;
};
