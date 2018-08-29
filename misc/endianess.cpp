#include <iostream>


using namespace std;

union {
	int i;
	char c[sizeof(int)];
}x;

int main() {
 
	x.i = 1;
	if (x.c[0] == 1) 
		cout<<"LittleEndian\n";
	else 
		cout<<"Big endian\n";

return 0;	

}
