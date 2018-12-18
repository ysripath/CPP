#include <iostream>
#include <vector>
using namespace std;


int helper(int W, int N, std::vector<int> val, std::vector<int> wt, std::vector<int> *result)
{
	// Initialize the matrix
	// Rows represent different weights of items
	// Columns are from 0 to max weight increasing by 1 unit


	int T[N][W+1];
	
	int i = 0;
	int j = 0;
	cout<<W<<" "<<N<<endl;
	for ( i = 0; i < N; i++)
		for (j = 0; j <= W; j++)
			T[i][j] = 0;
	
	 // Display matrix
        for (i = 0; i < N; i++)
        {
                for (j = 0; j <=W; j++)
                        cout<<T[i][j]<<"\t";
                cout<<endl;
        }
	// intialize first columnn - capacity is 0
	for (i = 0; i < N; i++)
		T[i][0] = 0;
	
	// Initialize matrix for first item
	i = 0;
	for (j = 1; j <=W; j++)
	{
		if (wt[i] <= j)
			T[i][j] = val[i];
	}
	for (i = 1; i < N; i++)
	{
		for (j = 0; j <= W; j++)
		{
			// Check if weight of current item can be put into the bag
			if (wt[i] <= j)
			{
				// Compare values on including and excluding this item and storee the max value possible
				T[i][j] = max((val[i]+T[i-1][j - wt[i]]), T[i-1][j] );
			}
			
			else // weight of the item exceeds the capacity of the bag, just take the previous value from previous best for that capacity
			{
				T[i][j] = T[i-1][j];
			}
		}
	}
	

	// Display matrix
	for (i = 0; i < N; i++)
	{
		for (j = 0; j <=W; j++)
			cout<<T[i][j]<<"\t";
		cout<<endl;
	}


	// Update the items picked
	int aV = T[N-1][W];
	i = N-1;
	j = W+1;
	while (aV >= 0 && i >= 0 && j >=0)
	{
		if (T[i-1][j] == T[i][j])
		{
			i--;
			continue;
		}
		else
		{
			aV -= val[i];

			result->push_back(i);
			j = j-wt[i];
			i--;
			continue;
		}
	}
	return T[N-1][W];
	 
}


int main()
{
	cout<<"Enter total weight\n";
	int W;
	cin>>W;


	cout<<"Enter number of available items\n";
	std::vector<int> val;
	std::vector<int> weight;
	int N;
	cin>>N;
	cout<<"Enter weights and values of items\n";
	for (int i = 0; i < N; ++i)
	{
		int v;
		int w;
		cin>>w;
		cin>>v;
		weight.push_back(w);
		val.push_back(v);
	}

	std::vector<int> result;
	cout<<"Max values is "<<helper(W, N, val, weight, &result)<<endl;
	cout<<"Selected items\n";
	for(auto itr : result)
	{
		cout<<"Item "<<itr+1<<" with weight and value "<<weight[itr]<<" "<<val[itr]<<endl;
	}
}
