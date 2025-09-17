def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        itemPostion = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[itemPostion]:
                itemPostion += 1 
                nums[itemPostion] = nums[i] 

        return itemPostion + 1
