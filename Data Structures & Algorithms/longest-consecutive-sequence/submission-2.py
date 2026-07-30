class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) ==0:
            return 0
        nums.sort()
        seq,seq1 = 1,1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            elif nums[i]+1 == nums[i+1]:
                seq1 += 1
            else:
                seq = max(seq,seq1)
                seq1 = 1
        return max(seq,seq1)
        
            
                

        