#include <iostream>
#include <boost/asio.hpp>
#include <boost/date_time/posix_time/posix_time.hpp>
#include <pthread.h>

using namespace std;

void* util(void* i) {
	for (int i = 0; i < 10; i++)
		cout<<i<<endl;
	pthread_exit(NULL);
}

int main()
{
  boost::asio::io_service io;
	boost::asio::deadline_timer t(io, boost::posix_time::seconds(5));

	pthread_t thread;
	int i = 1;
	int rc = pthread_create(&thread, NULL, util, (void*)i);
	if (rc)
		cout<<"Error creatiung thread "<<rc<<endl;

	  t.wait();
	std::cout << "Hello, world!\n";

  return 0;
}

