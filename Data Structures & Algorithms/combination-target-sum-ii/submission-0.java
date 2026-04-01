class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(candidates);
        combinationSum22(candidates, target, 0, new ArrayList<>(), result);
        return result;

    }

    private void combinationSum22(int[] candidates, int target, int indx, List<Integer> ans, List<List<Integer>> result) {
        if (target == 0) {
            result.add(new ArrayList<>(ans));
            return;
        }
        
        if (target < 0 || indx == candidates.length) return;

        for (int i = indx; i < candidates.length; i++) {
            if (i > indx && candidates[i] == candidates[i-1]) continue;
            
            int val = candidates[i]; 
            ans.add(val);
            combinationSum22(candidates, target-val, i+1, ans, result);
            ans.remove(ans.size() - 1);
        }

    }
}
