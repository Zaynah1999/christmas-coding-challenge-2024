def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    Length_of_array = len(nums)
    for i in range(Length_of_array):
        for j in range(Length_of_array):
            if i != j:
                if (nums[i] + nums[j]) == target:
                    return i, j