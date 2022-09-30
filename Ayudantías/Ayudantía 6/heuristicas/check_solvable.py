def getInvCount(arr, size):
    inv_count = 0
    empty_value = 0
    for i in range(0, size):
        for j in range(i + 1, size):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count
 
     
# This function returns true
# if given 8 puzzle is solvable.
def isSolvable(puzzle, size) :
 
    # Count inversions in given 8 puzzle
    inv_count = getInvCount([j for sub in puzzle for j in sub], size)
 
    # return true if inversion count is even.
    return (inv_count % 2 == 0)