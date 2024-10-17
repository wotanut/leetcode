class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        resetM = m
        for index,element in enumerate(nums1):
            if len(nums2) == 0:
                break
            elif nums2[0] <= element or (index >= m and element == 0):
                print(nums1, nums2, element, index, m)
                nums1.insert(index,nums2[0])
                nums2.remove(nums2[0])
                m = m + 1
        while nums1[-1] == 0:
            nums1.pop()
        while len(nums1) != resetM + n:
            nums1.append(0)

# I beat 100% of solutions with a time complexity of O(M+N) and a runtime of 12ms :DDDDDDD
