class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        int left = 0, count = 0;
        Set<Character> set = new HashSet<>();
        
        for (int right = 0; right < n; right++) {
            while (set.contains(s.charAt(right))) {
                set.remove(s.charAt(left));
                left++;
            }
            set.add(s.charAt(right));
            count = Math.max(count, right - left + 1);
        }

        return count;
    }
}
