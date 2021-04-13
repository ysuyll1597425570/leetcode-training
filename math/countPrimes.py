class solution:
    def countPrimes(self, n):
        is_primes = [1]*n
        count = 0
        for i in range(2, n):
            if is_primes[i]:
                count += 1
                for j in range(i*i, n, i):
                    is_primes[j] = 0
        return count


