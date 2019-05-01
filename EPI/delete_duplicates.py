#Delete duplicates from a sorted array, return number of elements 
"""
O(N) - Time and space solution
Use stack, only append to stack if last element of stack is different than cur element 
"""

def delete_duplicates_1(arr):
    if not arr:
        return []
    stack = [arr[0]]
    for i in range(1,len(arr)):
        if stack[-1] != arr[i]:
            stack.append(arr[i])
    return len(stack)


"""
O(N)- Time, O(1)- Space
Check if arr[write_index-1] is the same as current element, if not, change next write index element to cur element and 
increase write index

[0,1,1,2]
[0,1,2,2]
"""
def delete_duplicates_2(arr):

    if not arr:
        return 0

    write_index = 1

    for i in range(1,len(arr)):
        if arr[write_index-1] != arr[i]:
            arr[write_index] = arr[i]
            write_index += 1
    return write_index

print(delete_duplicates_2([0,0,1,1,2,3,4,5,5,6,6,6]))

