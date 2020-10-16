'''Problem Link - https://leetcode.com/problems/sort-colors/
Based on Dutch National Flag Algorithm'''

def sortColors(nums):
    low,high,mid = 0,len(nums)-1,0
    while mid<=high:
        if nums[mid] == 0:
            nums[mid],nums[low] = nums[low],nums[mid]
            low += 1;mid += 1
        elif nums[mid] == 2:
            nums[mid],nums[high] = nums[high],nums[mid]
            high -= 1
        else:
            mid += 1
    return nums

print(sortColors([2,0,2,1,1,0])) #[0, 0, 1, 1, 2, 2]
print(sortColors([2,0,1])) #[0, 1, 2]
