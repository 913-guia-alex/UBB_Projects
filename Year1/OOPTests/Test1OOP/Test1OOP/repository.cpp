#include "repository.h"

Repo::Repo()
{
}

//This function adds a new bill to the bill list , if an existing bill with the 
//same serial number exists the function doesn't add the bill
void Repo::addBill(Bill c)
{
	this->elems.push_back(c);
}


std::vector<Bill> Repo::getBillsSorted() {
	std::vector<Bill> orderedBills = elems;
	std::sort(orderedBills.begin(), orderedBills.end(), [](Bill a, Bill b) {
		return a.getName() < b.getName();
		});
	return orderedBills;
}

//This function sorts the bill list filtering the paid bills 
std::vector<Bill> Repo::getBillsPaid() {
	std::vector<Bill> PaidBills;
	for (const Bill& bill : elems) {
		if (bill.getPaid()=="true") {
			PaidBills.push_back(bill);
		}
	}
	return PaidBills;
}


std::vector<Bill> Repo::getBills()
{
	return this->elems;
}
