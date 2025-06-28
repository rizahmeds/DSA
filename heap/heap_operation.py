from typing import List


def get_parent(index):
    return (index-1)//2

def get_left_index(index):
    return (2*index)+1

def get_right_index(index):
    return (2*index)+2

def min_heapify(arr, index, size):
    smallest = index
    left = get_left_index(index)
    right = get_right_index(index)

    if left < size and arr[left] < arr[smallest]:
        smallest = left
    if right < size and arr[right] < arr[smallest]:
        smallest = right
    if smallest != index:
        arr[index], arr[smallest] = arr[smallest], arr[index]
        min_heapify(arr, smallest, size)

def heap_insertion(heap_arr: List, ele: int):
    heap_arr.append(ele)
    current = len(heap_arr) - 1
    while current > 0 and heap_arr[current] < heap_arr[get_parent(current)]:
        heap_arr[current], heap_arr[get_parent(current)] =  heap_arr[get_parent(current)], heap_arr[current]
        current = get_parent(current)

def delete_heap(heap_arr: List):
    last = len(heap_arr)-1
    if last < 1:
        heap_arr.pop()
        return
    
    heap_arr[0], heap_arr[last] = heap_arr[last], heap_arr[0]
    heap_arr.pop()
    for i in range(len(heap_arr)//2-1, -1, -1):
        min_heapify(heap_arr, i, len(heap_arr))


if __name__ == "__main__":
    arr = [10, 5, 15, 2, 20, 30]
    heap_arr = []
    for ele in arr:
        heap_insertion(heap_arr, ele)
    print("Heap array:", heap_arr) #[2, 5, 15, 10, 20, 30]

    delete_heap(heap_arr)
    print("After deletion array:", heap_arr) #[5, 10, 15, 30, 20]
    


