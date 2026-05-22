class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for i, num in enumerate(nums):
            remain = target - num
            if remain in count:
                return [count[remain], i]
            count[num] = i


        