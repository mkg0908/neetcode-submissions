class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i,j in enumerate(nums):
            num=target-j
            if num in hashmap:
                return [hashmap[num],i]
            hashmap[j]=i
            

