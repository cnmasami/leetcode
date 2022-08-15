# 编写一个算法来判断一个数 n 是不是快乐数。
#
# 「快乐数」定义为：
#
# 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
# 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
# 如果这个过程 结果为1，那么这个数就是快乐数。
# 如果 n 是 快乐数 就返回 true ；不是，则返回 false 。

class Solution:
    # 使用哈希集合检测循环
    # 有三种可能
    # 1. 最终会得到1
    # 2. 最终会进入循环
    # 3. 值会越来越大，最后接近无穷大
    # 我们怎么知道下个数会继续变大而不是最终得到1？
    # 可以仔细想一想，每一位数的最大数字的下一位数是多少
    # 当数字是个位数时，最大的数字是9，下一个数字是81
    # 当数字是两位数时，最大的数字是99，下一个数字是162
    # 当数字是三位数时，最大的数字是999，下一个数字是243
    # 当数字是四位数时，最大的数字是9999，下一个数字是324
    # 当数字是13位数时，最大的数字是9999999999999，下一个数字是1053
    # 对于3位数的数字，他的下一个数字不可能大于243，
    # 这意味着它要么被困在243一下的循环内，要么最终到达1
    # 如果是4位或者4位以上的数字，在每一步都会丢失1位，直到降到3位为止
    # 所以最坏的情况，算法可能会在243以下的所有数字上循环，而不会无限期的增大
    def isHappy(self, n: int) -> bool:
        """
        # 1. 按照题目要求做数位分离求平方和
        # 2. 使用哈希集合，每次生成链表中的下一个数字时，都检查它是否已经在哈希集合中
        # 如果不在哈希集合中，添加它
        # 如果在哈希集合中，意味着我们处于一个循环中，此时返回False
        # 使用哈希集合而不是向量，列表或者数字的原因时因为我们反复检查其中是否存在某数字
        # 检查数字是否在哈希集合中需要O（1）的时间
        # 而对于其他数据结构，则需要O(n)的时间
        # 选择正确的数据结构是解决这些问题的关键部分
        :param n:
        :return:
        """
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, mod = divmod(n, 10)
                total_sum += mod ** 2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1

    # 既然知道有循环，那么用环形链表的快慢指针法
    def pointer_isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, mod = divmod(n, 10)
                total_sum += mod ** 2
            return total_sum

        slow = n
        fast = get_next(n)

        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

        return fast == 1

    # 数学
    # 下一个值可能比自己大的最大数字是什么？根据之前的分析，知道它必须低于243
    # 因此，我们知道任何循环都必须包含小于243的数字，用这么小的数字
    # 编写一个能找到所有周期的强力程序，可以得到
    # 只有一个循环4→16→37→58→89→145→42→20→4
    # 所有其他数字都在进入这个循环的链上，或者在进入1的链上
    # 硬编码一个包含这些数字的散列集，到达其中一个数字，就知道在循环中
    def math_isHappy(self, n: int) -> bool:
        cycle_members = {4, 16, 37, 58, 89, 145, 42, 20}

        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2

            return total_sum

        while n != 1 and n not in cycle_members:
            n = get_next(n)

        return n == 1



a = Solution().isHappy(2)
print(a)
