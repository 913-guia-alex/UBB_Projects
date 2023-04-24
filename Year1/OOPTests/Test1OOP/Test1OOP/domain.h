#pragma once
#include <string>

class Bill {
private:
	std::string name;
	std::string serial_number;
	float sum;
	std::string paid;
public:
	Bill(std::string _name, std::string _serial_number, float _sum, std::string _paid);

	std::string getName() const;
	std::string getSerialNumber() const;
	int getSum() const;
	std::string getPaid() const;

	void setName(std::string newName);
	void setSerialNumber(std::string newModel);
	void setSum(int newYear);
	void setPaid(std::string newColour);

	std::string toStr() const;


};