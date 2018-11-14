class Solution {
public:
    string modify(string str)
{
	bool flag = false;
	bool pFlag = false;
	string temp = "";
	int l = str.length();
	int i = 0;
	int k = 0;

	while (i < l)
	{
		if (str[i] != '.' && str[i] != '+' && str[i] != '@')
		{
			temp  += str[i++];
			continue;
		}
		else if (str[i] == '.')
		{
			if (flag)
			{
				temp += str[i++];
				continue;
			}
			else
			{
				i++;
				continue;
			}
		}
		else if (str[i] == '+')
		{
			while (str[i] != '@')
			{
				i++;
			}
			flag = true;
			temp += str[i++];
			continue;
		}
		else if (str[i] == '@')
		{
			temp += str[i++];
			flag = true;
		}
	}
	return temp;
}
    int numUniqueEmails(vector<string>& emails) {
        set<string> s;
        auto itr = emails.begin();
        while (itr != emails.end())
        {
            string temp = modify(*itr);
            s.insert(temp);
            itr++;
        }
        
        return s.size();
    }
};
