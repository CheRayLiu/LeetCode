# Your previous Plain Text content is preserved below:
# 
# [Ints], Int
# 
# [1,2,4,2,5,6], 5
# [1->2, 4->6] => 2
# 
# [1,2,4,2,5,6], 1 => 1
# 
# [1,2,4,2,5,6,9], 9 => 3
# [1->2, 4->6, 9->9], 9 => 3
# 
# [1,2,4,5,2,6], 51 => -1
# 
# [1,2,4,2,5,6]
# [1,2,2,4,5,6]
# 

def target_belong(a,target):
    a = set(a)
    a = list(a) 
    a.sort()
    left = a[0]
    interval = []
    for i in range(len(a)-1):
        if a[i]+1 != a[i+1]:
            right = a[i]
            interval.append([left,right])
            left = a[i+1]
    right = a[-1]
    if left < right: 
        interval.append([left,right])
    else:
        interval.append([left,left])
    left = 0
    right = len(interval)-1
    print(interval)
    while (left <= right):
        mid = left + (right-left)//2
        if interval[mid][0] <=  target <= interval[mid][1]:
            return mid
        elif interval[mid][0] >  target:
            right -=1
        elif interval[mid][1] < target:
            left +=1
    return -1

import bisect

def solution(arr, n):
    # O(n) lookup
    if n not in arr:
        return -1
    # O(n logn) sort. Assuming in place
    arr.sort()
    idx = 1
    l = arr[0]
    intervals = []
    # O(n), only store starting of ranges because at this point n is guaranteed to be in the array
    while idx < len(arr):
        if arr[idx] - arr[idx-1] > 1:
            intervals.append(l)
            l = arr[idx]
        idx += 1
    intervals.append(l)
    return bisect.bisect_right(intervals, n) 