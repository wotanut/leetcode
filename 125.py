class Solution:
    def isPalindrome(self, s: str) -> bool:
        """https://leetcode.com/problems/valid-palindrome/"""
        validChars = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
        ]
        s = s.lower()
        s = s.strip(" ")
        sReversed = ""
        realS = ""
        for char in s:
            if char in validChars:
                realS = realS + char
                sReversed = char + sReversed
        print(sReversed)
        if realS == sReversed:
            return True
        else:
            return False
