#include <crtdbg.h>
#include <stdio.h>
#include "main.h"
#include "ui.h"
#include "tests.h"

int main() {
    testAll();
    setbuf(stdout, NULL);
    start();
    _CrtDumpMemoryLeaks();
    return 0;
}