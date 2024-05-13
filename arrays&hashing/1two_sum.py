from typing import List
def twoSum(self, nums: List[int], target: int) -> List[int]:
    # brute force: O(n^2)
    # sort then two pointers O(nlogn)
    # opt should be extended from the brute froce approach, the essence is that for each num, what we are looking for is target - num, plus dictionary lookup is O(1) constant time -> use hash map to store the seen numbers -> key: val for lookup, val: index
    # op takes O(n)
    seen = {}
    for i in range(len(nums)):
        num = nums[i]
        if (target - num) in seen:
            return [i, seen[target-num]]
        else:
            seen[num] = i
    return []
