#母牛生产
#题目描述：假设农场中成熟的母牛每年都会生 1 头小母牛，并且永远不会死。第一年有 1 只小母牛，
#从第二年开始，母牛开始生小母牛。每只小母牛 3 年之后成熟又可以生小母牛。给定整数 N，求 N 年后牛的数量。

class solution:
    def cow_amount(n:int):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3
        d = [0]*n
        d[0] = 1
        d[1] = 2
        d[2] = 3
        for i in range(3,n):
            d[i] = d[i-1] + d[i-3]
        return d[n-1]