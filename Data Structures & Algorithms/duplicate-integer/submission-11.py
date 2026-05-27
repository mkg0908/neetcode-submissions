class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # numsset=set()
        # for i in nums:
        #     if i in numsset:
        #         return True
        #     numsset.add(i)
        # return False

        return len(set(nums))<len(nums)