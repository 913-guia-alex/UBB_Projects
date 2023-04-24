#pragma once
#pragma once
#include "service.h"

class UI {
private:
	Service* serv;

public:
	UI(Service* serv);
	void printMenu();

	void addBill();

	void showBills();

	void showBillsPaid();

	void showBillsSorted();

	void run();
};