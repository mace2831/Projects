from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numind = {}
        results = []

        for index, value in enumerate(nums):
            if(target - value) not in numind:
                numind[value] = index
            else:
                results.append(numind[target - value])
                results.append(index)
        return results

if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9))
    print(sol.twoSum([3,2,4], 6))
    print(sol.twoSum([3,3], 6))
