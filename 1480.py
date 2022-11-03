
'''''
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        return nums


print(Solution().runningSum([1,2,3,4,5,6,7,8,9,10]))

'''''


def runningSum(nums: list[int]) -> list[int]:
    n = len(nums)
    for i in range(1, n):
        nums[i] += nums[i - 1]
    return nums

#  函数和方法的唯一区别就是：函数的参数列表里没有self


print(runningSum([1,2,3,4,5,6,7,8,9,10]))

