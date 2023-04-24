# 学生出勤记录 I
# 给你一个字符串 s 表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。记录中只含下面三种字符：
#
# 'A'：Absent，缺勤
# 'L'：Late，迟到
# 'P'：Present，到场
# 如果学生能够 同时 满足下面两个条件，则可以获得出勤奖励：
#
# 按 总出勤 计，学生缺勤（'A'）严格 少于两天。
# 学生 不会 存在 连续 3 天或 连续 3 天以上的迟到（'L'）记录。
# 如果学生可以获得出勤奖励，返回 true ；否则，返回 false 。
#


class Solution:
    def checkRecord(self, s: str) -> bool:
        a_count = l_count = 0

        for i in range(len(s)):
            if s[i] == 'A':
                a_count += 1
                if a_count >= 2:
                    return False
            elif s[i] == 'L':
                if i == 0 or s[i] == s[i-1]:
                    l_count += 1
                elif s[i] != s[i-1]:
                    l_count = 1

                if l_count >= 3:
                    return False

        return True

    # 官解
    def offical(self, s: str) -> bool:
        absent = late = 0
        for c in s:
            if c == 'A':
                absent += 1
                if absent >= 2:
                    return False
            elif c == 'L':
                late += 1
                if late >= 3:
                    return False
            else:
                late = 0

        return True


a = Solution().checkRecord('PPALLL')
print(a)


