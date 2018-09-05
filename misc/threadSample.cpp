#include <iostream>
#include <pthread.h>
#include <cstdlib> 
#include <unistd.h>
#define THREAD_NUM 100

int gCount = 0;
using namespace std;
void* hello2(void* i) {
	cout<<"33333 from thread number "<<(long)i<<endl;
	pthread_exit(NULL);

}

void* hello1(void *i) {

gCount++;
        if (gCount >= 10)
        {
                cout<<"Thread limit reached\n";
		exit(0);
                pthread_exit(NULL);
		
        }
        cout<<" 22222   From  thread number "<<(long)i<<endl;
        pthread_t threads[THREAD_NUM];
        int rc;
        for (int i = 0; i < THREAD_NUM; i++) {
                rc = pthread_create(&threads[i], NULL, hello2, (void*)i+1);
                if (rc)
                        cout<<"Error creating thread "<<rc<<endl;

	usleep(100);
        } 
        pthread_exit(NULL);



}


void* hello(void *i) {
	gCount++;
	if (gCount >= 10)
	{
		cout<<"Thread limit reached\n";
		exit(0);
		pthread_exit(NULL);
		
	}
        cout<<"11111111111 From  thread number "<<(long)i<<endl;
	pthread_t threads[THREAD_NUM];
	int rc;
	for (int i = 0; i < THREAD_NUM; i++) {
		rc = pthread_create(&threads[i], NULL, hello1, (void*)i+1);
		if (rc)
			cout<<"Error creating thread "<<rc<<endl;

		usleep(100);
	} 
        pthread_exit(NULL);

}

int main()
{
        cout<<"Hello world\n";
        pthread_t threads[THREAD_NUM];

        int rc;
        int i;

        for (int i = 0; i < THREAD_NUM; i++)
        {
                cout<<"Main creating thread - "<<i+1<<endl;
                rc = pthread_create(&threads[i], NULL, hello, (void*)i+1);
                if (rc) {
                        cout<<"Error creating thread "<<rc<<endl;
                }
		usleep(100);
        }

        return 0;
}

