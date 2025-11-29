# Merge Sort - Common Pitfalls and Learning Journey

## My Initial Approach

I broke down the merge sort problem into two separate parts:
1. **Divide**: Recursively split the array into smaller subarrays
2. **Conquer/Merge**: Merge two sorted subarrays into one sorted array

I tested my logic incrementally with:
- Single elements → Two elements
- Three elements → Four elements

This helped me understand each part independently before combining them.

---

## Where I Got Stuck (and What I Learned)

### Problem 1: `None` values in the merge function

**What happened:** When `conquer()` was first called, both `left_array` and `right_array` were `None`.

**Why it happened:**
- The recursion goes all the way down to single-element arrays first
- My `divide()` function didn't have a base case that returned the array
- When an array had only 1 element, the `if len(unsortedArr) > 1` condition was false
- The function implicitly returned `None`

**The fix:**
```python
def divide(unsortedArr):
    if len(unsortedArr) > 1:
        # ... splitting logic ...
        return conquer(divide(left_array), divide(right_array))
    return unsortedArr  # Base case: return the single-element array
```

**Key learning:** In recursion, always define your base case explicitly!

---

### Problem 2: Only getting `[-13]` in the sorted output

**What happened:** Without the `extend()` lines, my sorted array only contained one element: `[-13]`.

**Why it happened:**
The merge loop uses `and` in its condition:
```python
while pointer1 < len(left_array) and pointer2 < len(right_array):
```

This means the loop **stops as soon as either pointer reaches the end**, leaving remaining elements unprocessed.

**Example with `[3, 7]` and `[6, -10]`:**
1. Compare `3 < 6` → append `3`, now `[3]`
2. Compare `7 < 6` → append `6`, now `[3, 6]`
3. Compare `7 < -10` → append `-10`, now `[3, 6, -10]`
4. Loop exits (pointer2 reached the end)
5. **`7` is left behind!** ❌

As recursion unwinds, these incomplete merges compound. Elements get progressively lost at each level, and only one "survivor" makes it through—in my case, `[-13]`.

**The fix:**
```python
new_array.extend(left_array[pointer1:])
new_array.extend(right_array[pointer2:])
return new_array
```

**Key learning:** After the merge loop, always append remaining elements from both arrays. Only one will have leftovers, but both extends are safe to call.

---

### Problem 3: "Won't leftover elements be out of order?"

**My concern:** If elements are left over in one array, how do I know they belong at the end? What if they're smaller than elements in the other array?

**The answer:** They're **guaranteed** to be in the correct position because:

1. Both `left_array` and `right_array` are **already sorted** (from recursive calls)
2. When the loop exits, we've just compared the current leftover element with the last element we appended
3. The leftover element was **larger**, which is why it wasn't appended yet
4. Since the array is sorted, **all remaining elements** are larger than what we've already merged
5. Therefore, we can safely append all leftovers to the end

**Example:**
- Merging `[3, 7, 10, 15]` and `[2, 5, 8]`
- Loop exits when right array is exhausted
- Last comparison: `10 < 8` → False (so `8` was appended)
- Leftovers: `[10, 15]`
- Since `10 > 8` and everything in `new_array` is `≤ 8`, both `10` and `15` belong at the end

**Key learning:** Pre-sorted subarrays are what make the simple `extend()` work correctly!

---

### Problem 4: "How does it return a single array?"

**My confusion:** I'm making two recursive calls (`divide(left_array)` and `divide(right_array)`), so how does it return just one array?

**The answer:** Each `divide()` call returns exactly **one array**:

```python
return conquer(divide(left_array), divide(right_array))
```

This line:
1. Evaluates `divide(left_array)` → returns one sorted array
2. Evaluates `divide(right_array)` → returns one sorted array
3. Passes both to `conquer()` → merges them into **one** sorted array
4. Returns that single merged array upward

**Recursion flow with `[3, 7, 6, -10]`:**
```
divide([3, 7, 6, -10])
├─ divide([3, 7]) → [3, 7]
│  ├─ divide([3]) → [3]
│  ├─ divide([7]) → [7]
│  └─ conquer([3], [7]) → [3, 7]
│
├─ divide([6, -10]) → [-10, 6]
│  ├─ divide([6]) → [6]
│  ├─ divide([-10]) → [-10]
│  └─ conquer([6], [-10]) → [-10, 6]
│
└─ conquer([3, 7], [-10, 6]) → [-10, 3, 6, 7]
```

At every level, two arrays get merged into one, bubbling up until the final sorted array reaches the top.

**Key learning:** The merge operation is what combines two results into one at each recursion level!

---

## Final Working Code

```python
def divide(unsortedArr):
    if len(unsortedArr) > 1:
        mid = len(unsortedArr) // 2
        left_array = unsortedArr[0:mid]
        right_array = unsortedArr[mid:]
        return conquer(divide(left_array), divide(right_array))
    return unsortedArr

def conquer(left_array, right_array):
    new_array = []
    pointer1 = pointer2 = 0
    
    while pointer1 < len(left_array) and pointer2 < len(right_array):
        if left_array[pointer1] < right_array[pointer2]:
            new_array.append(left_array[pointer1])
            pointer1 += 1
        else:
            new_array.append(right_array[pointer2])
            pointer2 += 1
    
    new_array.extend(left_array[pointer1:])
    new_array.extend(right_array[pointer2:])
    return new_array

unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
sortedArr = divide(unsortedArr)
print("Sorted array:", sortedArr)
```

---

## Key Takeaways

1. **Always define base cases explicitly** - Don't rely on implicit `None` returns
2. **Handle remaining elements after merging** - The loop exits early; extend both arrays
3. **Trust the pre-sorted property** - Leftovers are safe to append because subarrays are already sorted
4. **Each recursion level returns ONE array** - The merge operation combines two into one

---

## For Future Learners

If you're implementing merge sort and something seems off, check these common pitfalls:
- ✅ Do you have a proper base case?
- ✅ Are you extending remaining elements after the merge loop?
- ✅ Are you returning the merged result?
- ✅ Do you understand why pre-sorted subarrays make extending safe?

Happy sorting! 🚀
