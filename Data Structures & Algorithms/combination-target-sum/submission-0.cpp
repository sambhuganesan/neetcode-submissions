class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<int> subset;
        vector<vector<int>> res;

        combinations(0, nums, subset, res, target);
        return res;

    }

    void combinations(int start, vector<int>& nums, vector<int>& subset, vector<vector<int>>& res, int target) {
        if (target < 0) {
            return;
        }

        if (target == 0) {
            res.push_back(subset);
            return;
        }

        for (int i = start; i < nums.size(); i++) {
            subset.push_back(nums[i]);
            target = target - nums[i];
            combinations(i, nums, subset, res, target);
            subset.pop_back();
            target = target + nums[i];
        }
    }
};
