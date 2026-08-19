class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,number in enumerate(nums):
            compliment = target - number
            if compliment in seen:
                return sorted([seen[compliment],i])
            seen[number] = i

            
        

        