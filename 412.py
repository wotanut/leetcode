class Solution:
    """https://leetcode.com/problems/fizz-buzz/"""

    def fizzBuzz(self, n: int) -> List[str]:
        list = []
        current = 1
        while len(list) != n:
            if current % 3 == 0:
                if current % 5 == 0:
                    list.append("FizzBuzz")
                else:
                    list.append("Fizz")
            elif current % 5 == 0:
                list.append("Buzz")
            else:
                list.append(current.__str__)
            current += 1
        return list
