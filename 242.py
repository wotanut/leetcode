class Solution:
    """https://leetcode.com/problems/valid-anagram/"""

    def isAnagram(self, s: str, t: str) -> bool:
        tList = list(t)
        sList = list(s)
        if len(tList) != len (sList):
            return False
        tList.sort()
        sList.sort()
        if tList == sList:
            return True
        else:
            return False
