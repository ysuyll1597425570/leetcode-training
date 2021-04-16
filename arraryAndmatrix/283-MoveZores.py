class solution:
    def moveZeros(self, nums:List[int]):
        left = right = 0
        #同时向右移动保持相对顺序
        while right < len(nums):
        ##保证left左边全为非零，left——right间是全零
        ##找到下一个非零数与left位置的0交换
            if nums[right]:
                nums[right],nums[left] = nums[left],nums[right]
                left += 1
            right += 1
            

    
         