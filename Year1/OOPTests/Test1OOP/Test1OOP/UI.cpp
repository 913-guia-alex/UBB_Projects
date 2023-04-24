#include "UI.h"
#include <iostream>
#include <algorithm>

UI::UI(Service* serv)
{
	this->serv = serv;
}

void UI::printMenu()
{
	std::cout << "1. Add a new bill\n";
	std::cout << "2. Show all bills\n";
	std::cout << "3. Show bills sorted\n";
	std::cout << "4. Show bills paid\n";
	std::cout << "0. EXIT\n";
}

void UI::addBill()
{
	std::string name, serial_number, paid;
	float sum;

	std::cout << "Enter bill company_name: ";
	std::cin >> name;


	std::cout << "Enter bill serial_number: ";
	std::cin >> serial_number;


	std::cout << "Enter bill sum: ";
	std::cin >> sum;


	std::cout << "Enter bill paid: ";
	std::cin >> paid;


	try {
		this->serv->addBillServ(name, serial_number, sum, paid);
		std::cout << "Bill added successfully!\n";
	}
	catch (std::exception& e) {
		std::cout << "Error: " << e.what() << "\n";
	}
}

void UI::showBillsSorted()
{
	std::vector<Bill> bills = this->serv->getBillsSortedServ();
	if (bills.size() == 0) {
		std::cout << "No bills in the list!\n";
		return;
	}

	for (auto& bill : bills) {
		std::cout << bill.toStr() << "\n";
	}
}

void UI::showBillsPaid()
{
	std::vector<Bill> bills = this->serv->getBillsPaidServ();
	if (bills.size() == 0) {
		std::cout << "No paid bills in the list!\n";
		return;
	}

	float sumTotal = 0.0;
	for (auto& bill : bills) {
		std::cout << bill.toStr() << "\n";
		sumTotal = sumTotal + bill.getSum();
	}
	std::cout << "The total for the paid bills is: " << sumTotal << "\n";
}

void UI::showBills()
{
	std::vector<Bill> v = this->serv->getBillsServ();
	for (int i = 0; i < v.size(); i++) {
		std::cout << v[i].toStr();
	}
}


void UI::run() {
	bool running = true;
	while (running) {
		printMenu();
		int choice;
		std::cout << "Enter your choice: ";
		std::cin >> choice;
		switch (choice) {
		case 0:
			running = false;
			break;
		case 1:
			addBill();
			break;
		case 2:
			showBills();
			break;
		case 3:
			showBillsSorted();
			break;
		case 4:
			showBillsPaid();
			break;
		default:
			std::cout << "Invalid choice. Please try again.\n";
			break;
		}
	}
}