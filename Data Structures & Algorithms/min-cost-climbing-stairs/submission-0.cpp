class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();

        if (n == 0) return 0;
        if (n == 1) return cost[0];
        if (n == 2) return min(cost[0], cost[1]);

        vector<int> total_costs(n);

        total_costs[n-1] = cost[n-1];
        total_costs[n-2] = cost[n-2];

        for (int i = n-3; i >= 0; i--) {
            total_costs[i] = cost[i] + min(total_costs[i+1], total_costs[i+2]);
        }

        return min(total_costs[0], total_costs[1]);
    }
};
