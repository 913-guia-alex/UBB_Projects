#include <iostream>
#include "UI.h"
//#include "test.h"


int main() {
	//test();

	Repo* repo = new Repo();
	Service* serv = new Service(repo);
	serv->add5Bills();
	UI* ui = new UI(serv);
	ui->run();
	return 0;
}