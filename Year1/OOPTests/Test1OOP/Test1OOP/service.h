#pragma once
#pragma once
#include "repository.h"

class Service {
private:
	Repo* repo;

public:
	Service(Repo* r);

	// add a new car to the repository
	// if another car with the same model and year exists, the car is not added
	int addBillServ(std::string name, std::string serial_number, float sum, std::string paid);


	// get a list of all cars ordered by name and then by model
	std::vector<Bill> getBillsServ();

	// get a list of vintage cars ordered by model
	std::vector<Bill> getBillsSortedServ();

	//function that gets all the cars in the list
	std::vector<Bill> getBillsPaidServ();

	//function that adds 10 cars in the car list
	void add5Bills();


};
