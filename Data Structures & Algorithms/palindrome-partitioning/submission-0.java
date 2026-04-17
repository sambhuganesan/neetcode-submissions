class Solution {
    private boolean checkPalindrome(String s, int left, int right) {
        int i = 0;
        while (left +i < right-i-1) {
            if (s.charAt(left+i) != s.charAt(right-1-i)) return false;
            i++;
        }
        return true;
    }

    private void onePart(String s, int left, int right, List<String> res, List<List<String>> answer) {
        if (left == right) {
            answer.add(new ArrayList<>(res));
            return;
        }

        for (int i = 1; i <= s.length() - left; i++) {
            if (checkPalindrome(s, left, left+i)) {
                res.add(s.substring(left, left+i));
                onePart(s, left+i, right, res, answer);
                res.remove(res.size() - 1);
            }
        }
    }

    public List<List<String>> partition(String s) {
        List<List<String>> answer = new ArrayList<>();
        List<String> res = new ArrayList<>();
        onePart(s, 0, s.length(), res, answer);

        return answer;
    }
}
