from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counters = Counter(nums)
        return [counter[0] for counter in counters.most_common(k)]
        
        
            
        