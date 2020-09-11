""" Testing code to test bubblesort """
from bubblesort import bubble_sort

def test_bubble_sort():
    """ bubble_sort pytest """
    assert bubble_sort([1,1,2,3])==[1,1,2,3], "Test Failed" #Test 1
    assert bubble_sort([1,2,1,3])==[1,1,2,3], "Test Failed" #Test 2
    assert bubble_sort([3,2,1,1])==[1,1,2,3], "Test Failed" #Test 3
    assert bubble_sort([1,3,2,1])==[1,1,2,3], "Test Failed" #Test 4
