class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashet = set()

        for i in nums:
            if i in hashet:
                return True
            else:
                hashet.add(i)
        return False
    