#求解最大公约数
class solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            self.gcd(b, a%b)
    