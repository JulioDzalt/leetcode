'''
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''
# O(N) 
class Solution:
    def productExceptSelf(self, nums: list[int]) -> int:
        
        prefix = 1
        sufix = 1
        lst_prefix = list()
        lst_sufix = list()
        
        for n in nums:
            lst_prefix.append(prefix)
            prefix*=n

        '''
        nums = [1,2,3,4]
        lst_prefix = [prefix = 1, prefix *= nums[0] , prefix *= nums[1], prefix *= nums[2]]
        lst_prefix = [1,1,2,6]
        '''
        
        for n in nums[::-1]:
            lst_sufix.append(sufix)
            sufix*=n

        '''
        nums = [4,3,2,1]
        lst_sufix = [sufix = 1, prefix *= nums[0] , prefix *= nums[1], prefix *= nums[2]]
        lst_sufix = [1,4,12,24]
        '''

        lst_sufix = lst_sufix[::-1]

        '''
        lst_prefix = [1,1,2,6]
        lst_sufix = [24,12,4,1]
        '''

        r = []
        for i in range(len(lst_prefix)):
            r.append(lst_prefix[i]*lst_sufix[i])

        return r # [24, 12, 8, 6]
            
    print(productExceptSelf(None, [1,2,3,4]))
