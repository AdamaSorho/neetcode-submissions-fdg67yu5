class Solution {
    public boolean isPalindrome(String s) {
        int n = s.length();
        int left = 0, right = n - 1;

        while (left < right) {
            if (!isAphaNumeric(s.charAt(left))) {
                left++;
            }
            else if (!isAphaNumeric(s.charAt(right))) {
                right--;
            }
            else if (Character.toLowerCase(s.charAt(left)) != 
                        Character.toLowerCase(s.charAt(right))) {
                return false;
            }
            else {
                left++;
                right--;
            }
        }

        return true;
    }

    private boolean isAphaNumeric(char c) {
        return (c >= 'A' && c <= 'Z' ||
                c >= 'a' && c <= 'z' ||
                c >= '0' && c <= '9');
    }
}
