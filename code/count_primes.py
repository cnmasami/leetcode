# 给定整数 n ，返回 所有小于非负整数 n 的质数的数量 。

class Solution:
    def isPrime(self, x:int) -> bool:
        for i in range(2, x+1):
            if x % i == 0:
                return False
        return True
    # 枚举
    def enum_count_primes(self, n: int) -> int:
        ans = 0
        for i in range(2, n):
            ans += self.isPrime(i)

        return ans

    # 埃氏筛
    # 如果x是质数，那么大于x的倍数2x，3x。。一定不是质数，从这里入手
    # 假设isPrimes[i]表示数i是不是质数，如果是质数为1，否则为0
    # 从小到大遍历每个数，如果这个数为质数，则将其余所有的倍数都标记为合数（除了该质数本身），即0
    # 这样在运行结束的时候我们即能知道质数的个数
    # 这种方法显然不会将质数标记成合数
    # 另一方面，当从小到大遍历到数x时，倘若它是合数，则它一定是某个小于x的质数y的整数倍
    # 故根据此方法的步骤，我们在遍历到y时，就一定会在此时将x标记为isPrime[x]=0
    # 因此，这种方法也不会将合数标记成质数
    # 当然这里还能继续优化，对于一个质数x，如果按上文说的我们从2x开始标记其实是冗余的，
    # 应该直接从x*x开始标记，因为2x，3x，，，这些数一定在x之前就被其他数的倍数标记过了
    # 例如2的所有倍数，3的所有倍数等
    def eratosthenes_count_primes(self, n: int) -> int:
        is_primes = [1] * n
        ans = 0

        for i in range(2, n):
            if is_primes[i]:
                ans += 1
                for j in range(i*i, n, i):
                    is_primes[j] = 0

        return ans

    # 线性筛
    # 埃氏筛其实还是存在冗余的标记操作，比如对于45这个数，它会同时被3，5两个数标记为合数
    # 优化的目标就是让每个合数只被标记一次。
    # 相较于埃氏筛，需要多维护一个primes数组表示当前得到的质数的集合
    # 从小到大遍历，如果当前的数x是质数，就将其加入primes数组
    # 另一点与埃氏筛不同的是，标记过程不再仅当x为质数时才进行，而是对每个整数x都进行
    # 对于整数x，我们不再标记其所有的倍数x*x，x*（x+1），
    # 而是只标记质数集合中的数与x相乘的数，即x*primes0， x*primes1，
    # 且在发现x mod primesi=0的时候结束当前标记
    # 核心点在于：如果x可以被primesi整除，那么对于合数y=x*primesi+1而言，
    # 它一定在后面遍历到(x/primesi)* primesi+1这个数的时候会被标记
    # 其他同理，这保证了每个合数只会被其【最小的质因数】筛去，即每个合数被标记一次
    # 线性筛还有其他的扩展用途，比如【积性函数】
    def linear_count_primes(self, n: int) -> int:
        is_prime = [1] * n
        primes = []

        for i in range(2, n):
            if is_prime[i]:
                primes.append(i)

            for prime in primes:
                if i * prime >= n:
                    break
                is_prime[i*prime] = 0
                # 如果i可以被prime_x整除，那么对于i*（prime_x+1）而言
                # 它一定在后面遍历到 (i / prime_x) * prime_x+1这个数的时候会被标记
                if i % prime == 0:
                    break

        return len(primes)


a = Solution().linear_count_primes(20)
print(a)



