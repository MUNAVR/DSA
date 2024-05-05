def bubble_sorting(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] > nums[j]:
                nums[i],nums[j]=nums[j],nums[i]
    return nums

nums=[1,2,3,5,4,5,6,86]
j=bubble_sorting(nums)
print(j)

