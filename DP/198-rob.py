#198.打家劫舍 
class solution:
	def rob(self,nums):
        #数组为空
        if not nums:
            return 0
        #只有一个房间
        size = len(nums)
        if size == 1:
            return nums[0]
        #多个房间情况下，边界条件。
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,size):
        #状态转移方程
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        return dp[size-1]