#include <vector>
#include "domain.h"

Bill::Bill(std::string _name, std::string _serial_number, float _sum, std::string _paid)
{
	this->name = _name;
	this->serial_number = _serial_number;
	this->sum = _sum;
	this->paid = _paid;
}

std::string Bill::getName() const
{
	return this->name;
}

std::string Bill::getSerialNumber() const
{
	return this->serial_number;
}

int Bill::getSum() const
{
	return this->sum;
}

std::string Bill::getPaid() const
{
	return this->paid;
}


void Bill::setName(std::string x)
{
	this->name = x;
}


void Bill::setSerialNumber(std::string x)
{
	this->serial_number = x;
}


void Bill::setSum(int x)
{
	this->sum = x;
}


void Bill::setPaid(std::string x)
{
	this->paid = x;
}


std::string boolToStr(bool x) {
	if (x == true) {
		return "true";
	}
	return "false";
}

std::string Bill::toStr() const
{
	std::string sumStr = std::to_string(this->sum);

	return this->name + " | " + this->serial_number + " | " + sumStr + " | " + this->paid + "\n";
}

