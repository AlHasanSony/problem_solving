#977. Squares of a Sorted Array
# Problem link - https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        res=[]
        l,r= 0, len (nums) -1
         
        while l<= r:
            if nums[l] * nums[l] > nums [r] * nums [r]:
                res.append (nums[l]*nums[l])
                l+=1
            else:
                res.append(nums[r] * nums[r])
                r-=1
                                                     
        return res[::-1]  #make it reverse      