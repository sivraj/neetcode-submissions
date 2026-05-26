class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_count = len(nums)
        prefix_product = [1]*nums_count
        for i in range(1, nums_count):
            prefix_product[i] = nums[i-1] * prefix_product[(i-1)]

        suffix_product = [1] * nums_count
        for i in range(nums_count-2, -1, -1):
            suffix_product[i] = nums[i+1] * suffix_product[(i+1)]

        result = []
        for i in range(nums_count):
            result.append(suffix_product[i] *prefix_product[i])

        return result

            