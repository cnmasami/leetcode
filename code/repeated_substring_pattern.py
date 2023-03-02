# 重复的子字符串
# 给定一个非空的字符串 s ，检查是否可以通过由它的一个子串重复多次构成。

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        sub_len = 1
        # 因为这个字串要构成完整字符串，所以，他不会大于长度的一半
        while sub_len <= len(s) // 2:
            sub = s[:sub_len]
            if sub * (len(s) // sub_len) == s:
                return True
            else:
                sub_len += 1

        return False

    # 如果字符串S包含一个重复的子字符串，那么这意味着可以多次 “移位和换行”`字符串，并使其与原始字符串匹配。
    # 例如：abcabc
    # 移位一次：cabcab
    # 移位两次：bcabca
    # 移位三次：abcabc
    # 现在字符串和原字符串匹配了，所以可以得出结论存在重复的子串。
    # 基于这个思想，可以每次移动k个字符，直到匹配移动 length - 1 次。
    # 但是这样对于重复字符串很长的字符串，效率会非常低。
    #
    # 为了避免这种无用的环绕，可以创建一个新的字符串 str，它等于原来的字符串 S 再加上 S 自身，
    # 这样其实就包含了所有移动的字符串。
    #
    # 比如字符串：S = acd，那么 str = S + S = acdacd
    # acd 移动的可能：dac、cda。其实都包含在了 str 中了。就像一个滑动窗口
    # 一开始 acd (acd) ，移动一次 ac(dac)d，移动两次 a(cda)cd。循环结束
    # 所以可以直接判断 str 中去除首尾元素之后，是否包含自身元素。如果包含。则表明存在重复子串。
    # 为什么去掉首尾：
    # 整个过程其实就是模仿旋转的过程。头部是没开始旋转，到了尾部是旋转了一圈回到了初始状态。
    # 这两种情况都是原字符串，肯定不能考虑的呀

    # 假设字符串s是由s1+s2组成的，s+s后，str就变成了s1+s2+s1+s2，
    # 去掉首尾，破环了首尾的s1和s2，变成了s3+s2+s1+s4,此时str中间就是s2+s1,
    # 如果s是循环字串，也就是s1=s2,所以str中间的s2+s1就和原字符串相等。
    # 如果s不是循环字串，s1!=s2，那么s1+s2是不等于s2+s1的，也就是str中间不包含s

    # 如果S不包含重复的子字符串，则S本身就是所谓的“重复子字符串”（这里方便自己理解，视为重复一次，不深究= =），
    # str = S+S,说明S是str的重复子字符串，刨去str首尾两个字符之后（相当于分别破坏前一个S头部和后一个S尾部），
    # 不能满足str包含S。
    # 从题目可以知道重复字符串至少重复n（n>=2）次才满足，用s+s则至少2n次重复，
    # 破环第一个和最后一个，在n>=2的前提下2n-2>=n 恒成立,所以中间至少有一个重复n次的字符串。
    def repeatedSubstringPattern2(self, s: str) -> bool:
        return (s + s).find(s, 1) != len(s)


a = Solution().repeatedSubstringPattern('abcabcabcabc')
print(a)