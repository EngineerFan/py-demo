from collections import *


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        c = Counter()
        for i in range(lowLimit, highLimit + 1):
            tmp_list = list(str(i))
            s = 0
            for j in range(len(tmp_list)):
                s += int(tmp_list[j])
            if c.get(s, None):
                c[s] = c[s] + 1
            else:
                c[s] = 1
        print(c)
        return c.most_common(1)[0][1]


if __name__ == '__main__':
    so = Solution()
    print(so.countBalls(lowLimit=19, highLimit=28))
