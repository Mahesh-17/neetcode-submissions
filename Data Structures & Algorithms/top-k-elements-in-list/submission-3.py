class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        lst = []
        for i in nums:
            freq[i] += 1
        return sorted(freq, key = freq.get)[::-1][:k]

                
        
        
        