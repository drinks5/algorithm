from typing import List


import random



class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.sample(nums, 1)[0]
        larger = [n for n in nums if n > pivot]
        smaller = [n for n in nums if n < pivot]
        equal = [n for n in nums if n == pivot]

        if len(larger) >= k:
            return self.findKthLargest(larger, k)
        elif len(larger) + len(equal) >= k:
            return pivot
        else:
            return self.findKthLargest(smaller + equal, k - len(larger))
