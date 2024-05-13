def isAnagram(self, s: str, t: str) -> bool:
    # brute force: iterate through both, count and compare the hash map -> O(n)
    # edge: length not equal
    if len(s) != len(t):
        return False
    s_map = {}
    t_map = {}
    for i in range(len(s)):
        s_map[s[i]] = s_map.get(s[i], 0) + 1
        t_map[t[i]] = t_map.get(t[i], 0) + 1
    return s_map == t_map


# note: the implementation of == comparing two sets iterate through the elements in the set for loopup, so O(n) time complexity

# a slight optimization -> use only one hash map, iterate through s to populate the frequency (++), then iterate through t to decrement (--), finally check if there are any non-zero value in the hash map
# save one map space