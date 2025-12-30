class Solution {
    public int pivotIndex(int[] nums) {

        // total = left + right + current


        int total = 0, left = 0;

        for (int x : nums) {
            total += x;
        }

        for (int i = 0; i < nums.length; i++) {
            int right = 0;

            right = total - (left + nums[i]);
            
            if (left == right) {
                return i;
            }

            left += nums[i];

        }

        return -1;
    }

    public static void main(String[] args) {
        int[] nums = {1,7,3,6,5,6};
        Solution so = new Solution();
        so.pivotIndex(nums);
    }
}

// 28