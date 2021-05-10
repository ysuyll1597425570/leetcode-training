#给定一个正整数 n，将其拆分为至少两个正整数的和，
#并使这些整数的乘积最大化。 
#返回你可以获得的最大乘积。
class solution:
    def integerBreak(self,n:int):
        if n == 0:
            return 0
        elif n == 1:
            return 0
        else:
            dp = [0]*(n+1)
            dp[0] = 0
            dp[1] = 0
            for i in range(2,n+1):
                cur_max = 0
                for j in range(1,i):
                    cur_max = max(j*(i-j),j*dp[i-j])
                    dp[i] = max(dp[i],cur_max)
            return dp[n]
                  