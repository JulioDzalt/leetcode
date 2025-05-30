'''
349. Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.


Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
'''
# O(n)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = nums1
        l = nums2
        if(len(nums1) > len(nums2)):
            l = nums1
            s = nums2
        found = {}
        for i in range(len(s)):
            c = s[i]
            if(c in l):
                if (found.get(c) is not None):
                    found[c] =  found[c] + 1
                else:
                    found[c] = 1
        r = []
        r = list(found.keys())
        # for k in keys:
        #     count = found.get(k)
        #     for j in range(count):
        #         r.append(k)
        return r
        
