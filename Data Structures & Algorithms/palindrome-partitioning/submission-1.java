class Solution {
    private boolean checkPalindrome(String s, int left, int right) {
        int i = 0;
        while (left +i < right-i-1) {
            if (s.charAt(left+i) != s.charAt(right-1-i)) return false;
            i++;
        }
        return true;
    }

    private void onePart(String s, int currIndx, List<String> res, List<List<String>> answer) {
        boolean isLastStringPalindrome = checkPalindrome(res.get(res.size() -  1), 0, (res.get(res.size() -  1)).length());
        
        if (currIndx == s.length()) {
            if (isLastStringPalindrome){
                answer.add(new ArrayList<>(res));
            }
            return;
        }

        if (isLastStringPalindrome) {
            res.add("" + s.charAt(currIndx));
            onePart(s, currIndx + 1, res, answer);
            res.remove(res.size() - 1);
        }

        String oldValue = res.get(res.size() - 1);
        res.set(res.size() -1, res.get(res.size() -  1) + s.charAt(currIndx));
        onePart(s, currIndx + 1, res, answer);
        res.set(res.size() - 1, oldValue);
    }

    public List<List<String>> partition(String s) {
        List<List<String>> answer = new ArrayList<>();
        List<String> res = new ArrayList<>(List.of(s.substring(0, 1)));
        onePart(s, 1, res, answer);

        return answer;
    }
}
