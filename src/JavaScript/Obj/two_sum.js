

const twoSum = function(nums, target) {


    if (Object.keys(nums).length == 0) {
        return -1;
    }

    const checkList = {};
    checkList[nums[0]] = 0;


    for (let i = 1; i < nums.length; i++) {
        let need = target - nums[i];
        if (need in checkList) {
            return [checkList[need], i];
        }
        checkList[nums[i]] = i;
    }

}

const nums = [3,2,4];

console.log(twoSum(nums, 6));

// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]

// total = num + need
// need = total - num