# def removeDuplicates(nums):
#     convert = [i for n, i in enumerate(nums) if i not in nums[n+1:]]
#     expectedNums = (len(convert))
#     print(expectedNums)
#     print(convert)

# removeDuplicates([0,0,1,1,1,2,2,3,3,4])
# removeDuplicates([1,1,2])

def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        itemPostion = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[itemPostion]:
                itemPostion += 1 
                nums[itemPostion] = nums[i] 

        return itemPostion + 1
