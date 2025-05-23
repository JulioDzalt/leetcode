class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dir = {}
        for i in range(len(nums)):
            actual = nums[i]
    
            if(dir.get(actual) is not None):
                complement_to_tarjet_index = dir.get(actual)
                return [complement_to_tarjet_index, i]
            else:
                complement_to_tarjet = target - actual
                dir[complement_to_tarjet] = i
