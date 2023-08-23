from typing import List
import bisect
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        print(people)
        l=0
        r=len(people)-1
        no=0
        while l<=r:
            if people[l]+people[r]<=limit:
                l+=1
                r-=1
                no+=1
            else:
                r-=1
                no+=1
            

        return no         

        
s=Solution()
answer=s.numRescueBoats([3,2,2,1],3)
print(answer)