class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1 = set(nums)
        ls = 0
        for i in set1:
            if i-1 not in set1:
                length = 1
                while i+length in set1:
                    length += 1
                ls = max(ls,length)
        return ls

        
            
                

        