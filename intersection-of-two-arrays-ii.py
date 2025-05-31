'''
350. Intersection of Two Arrays II
Attempted
Easy
Topics
premium lock icon
Companies
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

'''
# O(x) TODO
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        s = nums1
        l = nums2
        if(len(nums1) > len(nums2)):
            l = nums1
            s = nums2
        dir_s = self.makedir(s)
        dir_l = self.makedir(l)

        r = []

        keys = list(dir_s.keys())
        for k in keys:
            if(k in dir_l.keys()):
                count = min(dir_s.get(k), dir_l.get(k))
                for j in range(count):
                    r.append(k)
        return r
    
    def makedir(self, l: list[int]) -> dir:
        dir = {}
        for i in range(len(l)):
            c = l[i]
            if(c in l):
                if (dir.get(c) is not None):
                    dir[c] =  dir[c] + 1
                else:
                    dir[c] = 1
        return dir

