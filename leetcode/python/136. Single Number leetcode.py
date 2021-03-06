
#problem -  https://leetcode.com/problems/single-number/


class Solution(object):
    def singleNumber(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x,y: x^y, nums)
    
    
 
 
 
 
 
 
 
 
    
# use set, O(n) space
# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         count = set()
#         for i in xrange(len(nums)):
#             if nums[i] in count:
#                 count.remove(nums[i])
#             else:
#                 count.add(nums[i])
#         return count.pop()

# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         return 2*sum(set(nums)) - sum(nums)


# use dict, O(n) space
# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         count = {}
#         for i in xrange(len(nums)):
#             count[nums[i]] = count.get(nums[i], 0) + 1
#         for k,v in count.items():
#             if v == 1:
#                 return k

# xor, O(1) space
