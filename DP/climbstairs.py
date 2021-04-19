#解法一 递归法 时间空间复杂度O(n)
class solution:
    def climbStairs(self,n):
        # 初始临界状态 f(0)=1 f(1)=1
        if n == 1 or n == 0:
            return 1
        else:
            #状态转移方程 f(x) = f(x-1)+f(x-2)
            return self.climbStairs(n-1) + self.climbStairs(n-2)
            
    def climbStairs_2(self,n):
        p,q = 0
        r = 1
        #滚动数组
        for i in range(n):
            p = q
            q = r
            r = p+q
        return r
     
        