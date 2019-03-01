#include <bits/stdc++.h>


using namespace std;
int firstMissingPositive(vector<int>& nums) {

	if (nums.size() == 0)
		return 1;


	int l = nums.size();
	for (int i = 0; i < l; i++)
	{
		int val = nums[i];

		if (val < 1 || val > l)
			continue;


		while (nums[val - 1] != val)
		{
			int nV = nums[val - 1];
			nums[val - 1] = val;
			val = nV;
			if (val < 1 || val >= l)
				break;
		}

	}

	if (nums[0] != 1)
		return 1;

	for (int i = 0; i < l; i++)
	{
		if (nums[i] != i + 1)
			return i + 1;
	}
	return l + 1;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);


	int xorVal = -1;
	vector<int> v {2, 1 };

	cout << firstMissingPositive(v);
	return 0;
}