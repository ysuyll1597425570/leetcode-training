#题目描述：有N个信和信封,它们被打乱，求错误装信方式的数量。
class solution:
    def error_amount(self,N:int):
        if N == 0:
            return 0
        elif N == 1:
            return 0
        elif N == 2:
            return 2
        else:
            dp = [0]*N
            dp[0] = 0
            dp[1] = 2
            for i in range(2,N):
                dp[i] = ((i-1)*dp[i-2] + (i-1)*dp[i-1])
            return dp[-1]


sol = solution()
amount = sol.error_amount(3)
print("amount = ",amount)
