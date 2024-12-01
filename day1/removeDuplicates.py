def removeDuplicates(nums):
    convert = [i for n, i in enumerate(nums) if i not in nums[n+1:]]
    expectedNums = (len(convert))
    print(expectedNums)
    print(convert)

removeDuplicates([0,0,1,1,1,2,2,3,3,4])
removeDuplicates([1,1,2])

