class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int max = 0;
        
        for (int num: piles) {
            max = Math.max(max, num);
        }

        int k = max;
        int left = 1, right = k;

        while (left <= right) {
            int mid = (left + right) / 2;

            int hours = 0;
            for (int num: piles) {
                hours += Math.ceil((double) num / mid);
            }

            if (hours <= h) {
                k = Math.min(k, mid);
                right = mid - 1;
            }
            else {
                left = mid + 1;
            }
        }

        return k;
    }
}
