# A good example of divide and conquer and recursion
# Given an array sort it using method merge sort
def merge_sort(nums):
    if len(nums) == 1: 
        return nums
    else: 
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        sorted_left = merge_sort(left)
        sorted_right = merge_sort(right)
        return merge(sorted_left, sorted_right)
     
# given two ordered arrays merge them 
def merge(nums1, nums2): 
    if not nums1: 
        return nums2
    if not nums2: 
        return nums1
    else:
        if nums1[0] < nums2[0]: 
            return nums1[:1] + merge(nums1[1:], nums2)
        else:
            return nums2[:1] + merge(nums1, nums2[1:])
            

print(merge([1, 3,5, 7], [2, 4, 6, 8, 9]))

print(merge_sort([9,5, 2, 4, 9, 10, 11, 34, 5,1]))   

print(merge_sort([9,-5, 2, 4, 9, 10, 11, -34, 5,1]))   