class Solution {
    public List<String> generateParenthesis(int n) {
        StringBuilder s = new StringBuilder();
        List<String> result = new ArrayList<>();

        backtrack(0, 0, n, s, result);

        return result;
    }

    private void backtrack(int openN, int closeN, int n, 
            StringBuilder s, List<String> result) {

        if (openN == n && closeN == openN) {
            result.add(s.toString());
            return;
        }

        if (openN < n) {
            s.append("(");
            backtrack(openN + 1, closeN, n, s, result);
            s.deleteCharAt(s.length() - 1);
        }

        if (closeN < openN) {
            s.append(")");
            backtrack(openN, closeN + 1, n, s, result);
            s.deleteCharAt(s.length() - 1);
        }
    }
}
