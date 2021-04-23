#213 打家劫舍2 动态规划
class solution:
    def rob(self,nums:List[int]):
        def robRange(start:int,end:int):
            #循环队列分两种情况，偷第一家和不偷第一家
            first = nums[start]
            second = max(nums[start],nums[start+1])
            for i in range(start+2,end+1):
                first,second = second,max(first+nums[i],second)
            return second
            
        if not nums:
            return 0
        size = len(nums):
        if size == 1:
            return nums[0]
        elif size == 2:
            return max(nums[0],nums[1])
        else:
            return max(robRange(0,size-1),robRange(1,size))