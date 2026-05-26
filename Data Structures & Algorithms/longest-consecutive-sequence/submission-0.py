class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        result = 0
        for num in nums:
            if num-1 not in nums:
                counter = 0
                current = num
                while current in nums:
                    counter +=1
                    current +=1
                result = max(result, counter)
        return result                