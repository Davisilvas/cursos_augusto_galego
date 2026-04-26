class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = {}

        for i in nums:
            # if nums[i] in seen:
            if seen.get(i):
                return True
            seen[i] = '1'
        return False
