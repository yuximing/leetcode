#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        // hash map
        unordered_map<int, int> hashMap;
        for (int i = 0; i < nums.size(); i++)
        {
            int comp = target - nums[i];
            if (hashMap.count(comp))
            { // check existance
                return {hashMap[comp], i};
            }
            hashMap[nums[i]] = i;
        }
        return {}; // in case of no answer
    }
};

int main()
{
    Solution sol;
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;

    vector<int> res = sol.twoSum(nums, target);
    if (!res.empty())
    {
        cout << "result:" << res[0] << ", " << res[1] << endl;
    }
}