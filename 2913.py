class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = len(nums)
        counter = 0
        for i in range(a):
            seen = set()
            for j in range(i,a):
                seen.add(nums[j])
                counter += len(seen) ** 2
        return counter