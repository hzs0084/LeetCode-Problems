nums = [2,11,15,7]
class Solution(object):
    def twoSum(self, nums, target):
        
        hashMap = {}

        for index, num in enumerate(nums):
            complement = target - num

            if complement in hashMap:
                return [hashMap[complement], index]
            
            hashMap[num] = index

        return

        
        # target = 9
solution = Solution()

print(solution.twoSum(nums, target=9))