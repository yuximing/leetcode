from typing import List
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # brute force: count all occurance
    # OR, sort -> O(nlogn)
    '''
    count = {}
    res = []
    for num in nums:
        count[num] = count.get(num, 0) + 1
    sorted_count = sorted(count.items(), key=lambda x:x[1], reverse=True)
    print(sorted_count)
    for i in range(k):
        res.append(sorted_count[i][0])
    return res
    '''
    count_map = {}
    temp = []
    res = []
    for num in nums:
        count_map[num] = count_map.get(num, 0) + 1
    for i in range(len(nums) + 1):
        temp.append([])
    for num, count in count_map.items():
        temp[count].append(num)
    i = 0
    j = len(temp) - 1
    while i < k:
        # empty, to the left
        if len(temp[j]) == 0:
            j -= 1
            continue
        # not empty, process
        else:
            res.extend(temp[j])
            i += len(temp[j])
            j -= 1
    '''
    another way of looping to get the result array:
    for i in range(len(temp) - 1, 0, -1):
        for n in temp[i]:
            res.append(n)
            if len(res) == k:
                return res
    '''
        
    return res

# op1: max heap O(k*logn)
# heapify: O(n) pop k times: k*logn -> better than nlogn (sorting)

# op2: BUCKET SORT
# *** i thought of this solution but the integer numbers may be too big -> too much space and unknown ***
# (if input values are bounded)
# 1, 1, 1, 2, 2, 100
# index of array [0, 1, 2, ... 100]
# occurence.     [0, 3, 2, ... 1  ]
# ^^ this way, still need to sort (unclear who are the top k), still need nlogn so i didnt persue this path

# a better bucket sort:
# 1, 1, 1, 2, 2, 100
# index of array(=>the count)
# [0, 1, 2, 3, 4, 5, 6] # max count is the length of the array
# list of numbers who have the corresponding count
# [0, [100], [2], [1], 0, 0, 0]