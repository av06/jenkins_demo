""" Driver code to run bubblesort """
from bubblesort import bubble_sort

arr = [64, 34, 25, 12, 22, 11, 90]

result = bubble_sort(arr)

print ("Sorted array is:")
for i in result:
    print ("%d" %i)
