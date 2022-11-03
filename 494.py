class Solution:
    #  def findTargetSumWays(self, nums: List[int], target: int) -> int:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sum = 0
        for i in nums: sum += i
        if sum < abs(target) or (sum + target) % 2 == 1: return 0
        return self.subsets(nums, (sum + target) // 2)

    def subsets(self, nums, sum):
        n = len(nums)
        dp = [0 for _ in range(sum + 1)]
        dp[0] = 1
        for i in range(1,n + 1):
            for j in range(sum,-1,-1):
                if j >= nums[i - 1]:
                    dp[j] = dp[j] + dp[j - nums[i - 1]]
                else:
                    dp[j] = dp[j]
        return dp[sum]

'''''
if __name__ == "__main__":
    #  env = Solution().findTargetSumWays([1,1,1,1,1], 3)
    #  print(env)
    print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))
'''''

print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))