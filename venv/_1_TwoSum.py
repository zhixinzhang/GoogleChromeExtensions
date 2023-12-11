from typing import List


class _1_TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {};
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                print('*****')
                return [numMap[complement], i]
            
            numMap[nums[i]] = i

        return [] 
        
result = _1_TwoSum().twoSum([2,7,11,15], 9)
print(result)