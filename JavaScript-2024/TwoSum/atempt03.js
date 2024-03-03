/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let obh = {}
    for (let i = 0; i < nums.length; i++) {
        if (target - nums[i] in obh) {
            return [obh[target - nums[i]], i]
        } else {
            obh[nums[i]] = i;
        }
    }
};
