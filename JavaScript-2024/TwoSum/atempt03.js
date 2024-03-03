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


// Runtime: 76 ms
// Runtime 48 ms
// Memory 50.54 MB
