#求解最大公约数和最小公倍数
class solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            self.gcd(b, a%b)
            
    
    
    def lcm(self, a, b):
        return a * b / self.gcd(a,b)
    