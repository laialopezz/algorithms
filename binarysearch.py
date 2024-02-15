
# Worst-case performance will be O(log n)
def binarySearch(list, itemToSearch):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high)//2 # Checking the middle element of the list
        guess = list[mid]
        if guess == itemToSearch:
            return mid # We return the position of the item to search 
        if guess > itemToSearch: # Guess too high
            high = mid - 1 
        else: # Guess too low
            low = mid + 1
    return None

list = [1,3,5,7,9]

print(binarySearch(list , 3)) # First positon found
print(binarySearch(list , -1)) # None
