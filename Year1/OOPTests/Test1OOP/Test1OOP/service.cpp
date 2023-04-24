#include "service.h"

Service::Service(Repo* repo)
{
    this->repo = repo;
}


int Service::addBillServ(std::string name, std::string serial_number, float sum, std::string paid) {
    std::vector<Bill> bills = this->repo->getBills();
    for (const auto& bill : bills) {
        if (bill.getSerialNumber() == serial_number || paid != "false" && paid != "true") {
            return false;
        }
    }
    Bill b(name, serial_number, sum, paid);
    this->repo->addBill(b);
}


void Service::add5Bills()
{
    Bill b1 = Bill("Digi Sport", "8U34GUHG", 75.0, "false");
    Bill b2 = Bill("E-On", "39RV8NYY8", 122, "true");
    Bill b3 = Bill("Orange", "X3RN9R3X9NH", 46, "true");
    Bill b4 = Bill("Vodafone", "3CRNUUYBC", 23, "true");
    Bill b5 = Bill("Tcomm", "CR3GG", 10, "false");

    this->repo->addBill(b1);
    this->repo->addBill(b2);
    this->repo->addBill(b3);
    this->repo->addBill(b4);
    this->repo->addBill(b5);
}


std::vector<Bill> Service::getBillsPaidServ()
{
    std::vector<Bill> allCars = this->repo->getBillsPaid();
    return allCars;
}

std::vector<Bill> Service::getBillsSortedServ()
{
    std::vector<Bill> allCars = this->repo->getBillsSorted();
    return allCars;
}

std::vector<Bill> Service::getBillsServ()
{
    return this->repo->getBills();
}
