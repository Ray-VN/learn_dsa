// class Solution1 {
//     public int[] runningSum(int[] nums) {
//         int[] list = new int[nums.length];
//         int sum = 0;

//         for (int i = 0; i < nums.length; i++) {
//             sum += nums[i];
//             list[i] = sum;
//         }

//         return list;
//     }

//     public static void main(String[] args) {
//         int[] nums = {3,1,2,10,1};
//         Solution1 so = new Solution1();
//         System.out.println(so.runningSum(nums));
//     }
// }

