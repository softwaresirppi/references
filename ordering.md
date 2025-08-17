# Sorting
Arranging items such that `previous <= next` property is preserved
WHERE `previous` and `next` can be any element in the array
	AND `previous` occurs before `next` in array
	
# By Insertion
take an element and insert it in the 'right' spot AGAIN and AGAIN

QuickSort: inserting in middle after partitioning 
TreeSort: inserting into a search tree 
HeapSort: inserting into a heap 
CountingSort: inserting or marking it in a counting array 
(NOTE: this requires the range of items beforehand)

# By Selection
take a spot and choose the 'right' element AGAIN and AGAIN

BubbleSort: select the element for right-most spot by bubbling 
MergeSort: select (merge) the elements after two partitions are already sorted recursively 

# Misc.
BogoSort: Doing insertion or selection RANDOMLY and hope god sorts it for you!
SleepSort: Perform a sleep competition with each number where the sleep time is proportional to itself, and note the order in which they wake up!


RadixSort: inserting into a hashmap who's hash function is hash(x) = x % 10. (in other words, bucketting based on last digit)
ShellSort:
CycleSort:
BuckerSort
