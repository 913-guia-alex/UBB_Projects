#pragma once
#include <vector>
#include <algorithm>
#include "domain.h"

class Repo {
private:
	std::vector<Bill> elems;
public:
	Repo();

	void addBill(Bill b);
	std::vector<Bill> getBills();
	std::vector<Bill> getBillsSorted();
	std::vector<Bill> getBillsPaid();

};