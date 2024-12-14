def searchInsert(self, nums: List[int], target: int) -> int:
    if target in nums:
        return nums.index(target)
    else:
        for n, num in enumerate(nums):
            if target < num:
                return n
        else:
            return n + 1