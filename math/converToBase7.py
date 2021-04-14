#10进制转化为7进制
class solution:
    def convertToBase7(self,num):
        if num == 0:
            return '0'
        res = ''
        sym = True
        if num < 0:
            sym = False
            num = abs(num)
        while num > 0:
            res = str(num%7) + res
            num = num // 7
        if sym:
            return res
        else:
            return '-'+res