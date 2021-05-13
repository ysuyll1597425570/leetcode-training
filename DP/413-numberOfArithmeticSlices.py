class solution:
    def numberOfArithmeticSlices(self,nums:List[int])：
        size = len(nums):
        if size<3:
             return 0
        dp = [0]*size]
        count = 0
        for i in range(2,size):
            if nums[i]-nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = d[i-1]+1
                count = count+dp[i]
            else:
                continue
        return count