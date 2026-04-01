from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        common_nums = counter.most_common(k)
        ans = []
        for num in common_nums:
            ans.append(num[0])
        return ans
        