class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        lst = nums.copy()

        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if lst[j] <= lst[j+1]:
                    continue
                else:
                    if bin(lst[j]).count("1") == bin(lst[j+1]).count("1"):
                        lst[j], lst[j+1] = lst[j+1], lst[j]
                    else:
                        return False 
        return True