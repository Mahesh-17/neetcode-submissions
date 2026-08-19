class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dicti = {}
        # for i in range(len(nums)):
        #     comp = target - nums[i]
        #     if comp in dicti:
        #         return sorted([i,dicti[comp]])
        #     dicti[nums[i]] = i
        left = 0
        right = len(nums)-1
        nums = [(num, i) for i, num in enumerate(nums)]
        nums.sort()
        while left < right:
            total = nums[left][0]+nums[right][0]
            if total == target:
                return sorted([nums[left][1], nums[right][1]])
            elif total < target:
                left += 1
            else:
                right -= 1
        return []
            
        

        