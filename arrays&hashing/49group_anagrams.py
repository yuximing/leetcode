from typing import List
from collections import defaultdict
'''
TIME LIMIT EXCEEDED, could not solve it
'''
'''
def isAnagrams(self, s1, s2):
    # O(n)
    if len(s1) != len(s2):
        return False
    char_count = {}
    for c in s1:
        char_count[c] = char_count.get(c, 0) + 1
    for c in s2:
        char_count[c] = char_count.get(c, 0) - 1
    for val in char_count.values():
        if val < 0:
            return False
    return True
    
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # 1. how to check if two words are anagram -> hashmap, the count of char
    # 2. how to group them, iterate through the array, if no seen anagram group, create a new group; if yes, append to the anagram group
    # O(n^2)
    groups = []
    for s in strs:
        # edge case for the first str elem
        if len(groups) == 0:
            groups.append([s])
            continue
        found = False
        for group in groups:
            if self.isAnagrams(group[0], s):
                group.append(s)
                found = True
                break
        # no existing anagram
        if not found:
            groups.append([s])
    return groups
'''
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # {"pattern(1e 1a 1t)": ["eat", "ate", "tea"]}
    # O(m*n) where m is the total length of the array and n is the average length of each string (for each string, need to count to get the pattern)
    # since there are characters only, for the count(pattern) -> could just use an array of length 26 (here the constrain is that all letters are lowercase)
    # extra: what if the contraint is lifted?
    # could use ord? -> NO, may have the same number but different pattern
    # could use sort -> sorting the string could be the universal solution here
    groups = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        groups[tuple(count)].append(s) # list cannot be key in python dict, tuple is non-mutable
    return groups.values()
