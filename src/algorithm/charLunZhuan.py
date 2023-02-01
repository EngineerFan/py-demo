class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        else:
            pass


if __name__ == '__main__':
    so = Solution()
    s1 = 'waterbottle'
    s2 = 'erbottlewat'
    print(so.isFlipedString(s1=s1, s2=s2))
