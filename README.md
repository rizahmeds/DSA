# DSA
Data Structures and Algorithm using python.

# Selection of right data strcuture.

## Array
Array stores elements in contiguous memory location i.e one after the other. Element get stored at the end of the array which is constant time operation.
### When to use
1. Element lookup takes contant time when index is given and we know the size of the array.
2. Adding and removing element from the end of the array is also a constant time operation.
### When not to use
1. In order to add element at any other index of the array apart from end require us to move rest of the element which is a O(Len(Arr)-insertIndex) time operation. Which makes it not so much efficient when there are lots of elements to be moved.

## LinkList
Linklist consist of nodes. Nodes not stored in contiguous memory location rather they connect via pointer. Nodes have two parts, one part conatins the data and other part contains the pointer which points to the next node. First node is called the head node and the last node called tail node.
### When to use
1. For insertion we don't need to shift all the elements. We just have to adjust the pointers.
### When not to use
1. Searching for data is linear time operation. In worst case scenario it gives O(n) time complexity.

## Heap
Heap data structure should be a compelte binary tree and parent nodes are either greater than or equal to or less than or equal to their children, depending on whether it's a max-heap or min-heap. Root should be largest in max-heap and smallest in min-heap.
### When to use
1. 
### When not to use

## Priority Queue
In a priority queue, each element has an associated priority, which determines its order of service. Priority queue serves highest priority items first.







