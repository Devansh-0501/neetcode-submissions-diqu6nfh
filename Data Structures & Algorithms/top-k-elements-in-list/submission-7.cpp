class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map <int,int> count;
        vector <int> v;
        vector<vector<int>> t(nums.size() + 1);
        int j=0;
        for(int i=0;i<nums.size();i++)
        {
            count[nums[i]]++;
        }
        
        for(auto i : count)
        {
            t[i.second].push_back(i.first);
        }
        
        for(int j=t.size()-1;j>0;j--)
        {
           for (int n : t[j]) 
           {
                v.push_back(n);
                if (v.size() == k) {
                    return v;
                }
            }
       

    

        
        }
        return v;
      
    }
};
