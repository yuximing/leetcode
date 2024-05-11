from typing import List
def containsDuplicate(self, nums: List[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# time: O(n^2)? "if num in past" checking will iterate through past too
# space: O(n), array past takes n spaces

'''
reflection:
i initially used array, where the checking would take an extra O(n) time so didn't pass all test cases (time limit exceeded)

optimal solution -> hash set, average lookup costs O(1) only

note:
according to python time complexity wiki https://wiki.python.org/moin/TimeComplexity
x in s average costs O(1), worst case cost O(n)
'''