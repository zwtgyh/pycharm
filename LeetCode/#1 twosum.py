class Solution():
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i

class Solution():
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in nums:
                if i != nums.index(temp):
                    return [i, nums.index(temp)]
#测试
a = Solution()
a.twoSum([2,9,3,6,0], 9)
#都只能输出一组解