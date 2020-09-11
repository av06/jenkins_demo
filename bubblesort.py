""" Sorting Module """

def bubble_sort(array):
    """ Bubble Sort implementation. Input: List[Int] """
    list_size = len(array)

    # Traverse through all array elements
    for item in range(list_size-1):

        # Last i elements are already in place.
        for j in range(0, list_size-item-1):

            # Swap if the greater element with smaller element
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array
