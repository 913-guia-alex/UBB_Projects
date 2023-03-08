#include "ShortTest.h"
#include <assert.h>
#include <exception>
#include "Bag.h"
#include "BagIterator.h"


void testRemoveOccurences()
{
	Bag b;
	b.add(1);
	b.add(1);
	b.add(1);
	b.add(1);
	b.add(2);
	b.add(2);
	b.add(2);

	assert(b.removeOccurrences(4, 1) == 0);
	assert(b.removeOccurrences(5, 1) == 4);
	assert(b.size() == 3);
	assert(b.removeOccurrences(5, 3) == 0);

	try
	{
		b.removeOccurrences(-1, 3);
		assert(false);
	}
	catch (std::exception&) {
		assert(true);
	}
}


void testAll() {
	testRemoveOccurences();
	Bag b;
	assert(b.isEmpty() == true);
	assert(b.size() == 0); 
	b.add(5);
	b.add(1);
	b.add(10);
	b.add(7);
	b.add(1);
	b.add(11);
	b.add(-3);
	assert(b.size() == 7);
	assert(b.search(10) == true);
	assert(b.search(16) == false);
	assert(b.nrOccurrences(1) == 2);
	assert(b.nrOccurrences(7) == 1);
	assert(b.remove(1) == true);
	assert(b.remove(6) == false);
	assert(b.size() == 6);
	assert(b.nrOccurrences(1) == 1);
	BagIterator it = b.iterator();
	it.first();
	while (it.valid()) {
		TElem e = it.getCurrent();
		it.next();
	}
}
