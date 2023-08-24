from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        n=len(nums)-1
        nz=0
        while l<=n:
            if nums[l]!=0:
                nums[l],nums[nz]=nums[nz],nums[l]
                l+=1
                nz+=1
            else:
                l+=1

            
        print(nums) 

        
s=Solution()
s.moveZeroes([0,1,0,3,12])
# print(answer)