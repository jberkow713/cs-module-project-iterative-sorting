# runtime: O(n * n) = O(n^2)
def selection_sort(arr):
    # iterate through the array (represents the sorted-unsorted boundary 
    # moving across the array)
    for i in range(0, len(arr)):  # O(n)
        # index of the boundary, as well as the index we're going to 
        # swap the smallest element with 
        boundary = i
        smallest_value = arr[boundary]
        smallest_index = boundary
        # finding the smallest element 
        # in the "unsorted" portion of the array 
        # so as i gets bigger, you move from left to right, and 
        # you find the minimum value...get to the end of the list, 
        # bring the minimum value to the beginning of the list
        # But as i goes up, then the boundary goes up, and so when you find
        # the next min value, you move it not to the beginning of the total list,
        # but to the beginning of the unsorted list
        for unsorted_index in range(boundary, len(arr)):  # O(n)
            if arr[unsorted_index] < smallest_value:
                smallest_value = arr[unsorted_index]
                smallest_index = unsorted_index
        # `smallest_index` is the index of the smallest element in the unsorted portion
        # once that's found, swap it with the element on the right edge 
        # of the sorted-unsorted boundary
  
        arr[boundary], arr[smallest_index] = arr[smallest_index], arr[boundary]
    
    return (arr)       
            

        #smallest = smallest element in unsorted portion

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here


        # TO-DO: swap
        # Your code here

    


# TO-DO:  implement the Bubble Sort function below
#def bubble_sort(arr):


#    n = len(arr)
    # scroll through all values in array, sort first value with 2nd value, 2nd with 3rd
    # repeat process until all sorted
    
#    for i in range(len(arr)0, n- 1):


        # so we want to push the biggest value to the end of the list, reduce
        # size of list by 1 so that the biggest value is  not inside of the new search,
        #  and then start the scan over from the beginning
        # swapping a value with its next in line, if that value is bigger than its 
        #next in line value, repeat process until size = 1
            
        
#        for x in range(0, n-i-1):

#            if arr[x] > arr[x+1]:
#                arr[x], arr[x+1] = arr[x+1], arr[x]

#    return(arr)            

def bubble_sort(arr):
   
    for i in range (len(arr)-1, 0, -1):
        for j in range(i):

# scroll through the list, and swap one element with next element, if the first
# element is bigger than 2nd, then repeat
# it will go to element 0, and check to see is element 0 > element 1? 
# if so, swap them. Then it will go to element 1, say is element 1> element 2? 
# if so swap them, and as the outer list gets smaller,
# and reduces its length by 1,  the inner loop will run again, and again
#  and this will repeat until the length of the list is 1,
# and the elements will be sorted, and it will return the array
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return(arr)            

 
        
            

         

                

        





    

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
