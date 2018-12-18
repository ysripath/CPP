#include <iostream>
#include <vector>
using namespace std;


void helper(vector<vector<int>> &v, int i, int j, int A, int val)
{
	cout<<i<<" "<<j<<endl;
    if ( val == 1)
    {
        v[i][j] = val;
        return;
    }
    
    int lB = i;
    int rB = A-j;
    int bB = A-i;
    cout<<"rB "<<rB<<" bB"<<bB<<endl;
    
    // move right
    int row = i;
    for (int col = j; col <= rB; col++)
    {
        v[row][col] = val;
    }
    
    // move down
    int col = rB;
    for (int r = i; r <= bB; r++)
        v[r][col] = val;
    
    // bottom row
    row = bB;
    for (int c = j; c <= rB; c++)
        v[row][c] = val;
        
    //move up 
    col = j;
    for (int r = i; r <= bB; r++)
        v[r][col] = val;
    
    helper(v, i+1, j+1, A, val-1);
}


vector<vector<int> >prettyPrint(int A) {
    
    int N = 2*A-1;
    vector<vector<int>> result;
    for (int i = 0; i < N; i++)
    {
        vector<int> v;
        for (int j = 0; j < N; j++)
        {
            v.push_back(0);
        }
        result.push_back(v);
    }
    
    helper(result, 0, 0, N-1, A);
    return result;
    
    
}

int main()
{
cout<<"Enter A\n";
int A;
cin>>A;
vector< vector <int> > v = prettyPrint(A);
int N = v[0].size();
for (int i = 0; i < N; i++)
{
	for (int j = 0; j < N; j++)
		cout<<v[i][j]<<" ";
	cout<<endl;
}

return 0;
}
