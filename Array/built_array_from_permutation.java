

class Solution {
    public int[] buildArray(int[] nums) {
        int[] ins = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            ins[i] = nums[nums[i]];
        }

        return ins;
    }

    public static void main(String[] args){
        int[] nums = {0,2,1,5,3,4};

        Solution so = new Solution();
        System.out.println(so.buildArray(nums));
    }
}