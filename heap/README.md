## Heap data structure
Heap data structure is a complete binary tree, nodes at each level are fully filled except the last level, which is filled from left to right.

## Types of Heap
**<ins>Min Heap</ins>:** All the node element should be smaller than its childern elements.

**<ins>Max Heap</ins>:** All the node element should be greater than its childern elements.

## Operations
**<ins>Heapify</ins>:** Given an array, modify the array so that it will maintain the heap properties. Heapifing array depends upon type of heap. For Min heapify all the node elments should be smaller than its childern nodes. For Max heapify all the node elments should be greater than its childern nodes.

**<ins>Insertion</ins>:** Always apppend the element at the end of the array or last available leaf node from left to right. Perform the heapify operation the heap array so that it maintains the heap properties.

**<ins>Deletion</ins>:** Delete the root element of the heap by first swapping it with the last element then delete the last element. Perform the heapify operation over the heap array so that it maintains the heap properties.

## How heap work
It stored in array but represented as a complete binary tree, so to an array elements represent it into complete binary first. 
- Parent of any node i, is i//2.
- Left of any node i, is 2*i.
- Right of any node i, is (2*i)+1.
```
Example: [16,14,10,8,7,9,3,2,4]
Index:     1  2  3 4 5 6 7 8 9
Parent of value 3 is 8 i.e 6//2 = index 3 which is arr[3]=8.
Left of value 3 is 9 i.e 2*i = index 6 which is arr[6]=9.
Right of value 3 is 9 i.e (2*i)+1 = index 7 which is arr[8]=2.
```




