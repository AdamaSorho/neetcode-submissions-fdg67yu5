class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();
        int left = 0, right = nums.length - 1;

        while(left < right) {
            if (set.contains(nums[left])) {
                return true;
            }
            else {
                set.add(nums[left++]);
            }

            if (set.contains(nums[right])) {
                return true;
            }
            else {
                set.add(nums[right--]);
            }
        }

        return false;
    }
}
