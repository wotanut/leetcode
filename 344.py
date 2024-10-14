class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.

        https://leetcode.com/problems/reverse-string/
        """
        firstPointer = 0
        lastPointer = len(s) - 1
        while firstPointer < lastPointer:
            print(f"{firstPointer} {lastPointer}")
            tmp = s[firstPointer]
            s[firstPointer] = s[lastPointer]
            s[lastPointer] = tmp
            firstPointer += 1
            lastPointer += 1

