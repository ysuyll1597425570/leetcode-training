#给定一个整数数组  nums，求出数组从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点。
#实现 NumArray 类：
#NumArray(int[] nums) 使用数组 nums 初始化对象
#int sumRange(int i, int j) 返回数组 nums 从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点（也就是 sum(nums[i], nums[i + 1], ... , nums[j])）
class NumArray
    def _init_(self,nums:List[int]):
        self.nums = nums
        for i in range(1,len(nums)):
            self.nums[i] = nums[i] + self.nums[i-1]
    
    def sumRange(self,left:int,right:int):
        if left == 0:
            ans = self.nums[right]
        else:
            ans = self.nums[right] - self.nums[left-1]
        return ans