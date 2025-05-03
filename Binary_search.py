# Define the binary search function that searches for 'num' in the sorted list 'arr'
def search(arr, num):
    # Initialize the left and right pointers for the search range
    left = 0
    right = len(arr) - 1

    # Continue the search while the range is valid
    while left <= right:
        # Calculate the middle index
        mid = (left + right) // 2

        # Check if the middle element is equal to the number we're searching for
        if num == arr[mid]:
            print(f'Number {num} found at index {mid}')  # Output the result
            return  # Exit the function since the number is found

        # If the number is greater than the middle element, search in the right half
        elif num > arr[mid]:
            left = mid + 1  # Move the left boundary to mid + 1

        # If the number is less than the middle element, search in the left half
        else:
            right = mid - 1  # Move the right boundary to mid - 1

    # If the loop completes, the number is not found in the array
    print(f'Number {num} not found in the given array')

# Define a sorted list to perform the search on
arr = [1, 4, 6, 7, 9, 11, 18, 33, 55, 78]

# Call the search function to look for the number 78 in the array
search(arr, 78)
