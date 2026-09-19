class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for i in nums:
            hash[i] = hash.get(i, 0) + 1
        sorted_d = dict(
            sorted(hash.items(), key=lambda x: x[1], reverse=True)
        )
        return list(sorted_d)[:k]