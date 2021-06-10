import sys


def bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)


def selection_sort(arr):
    index = 0
    for i in range(len(arr)):
        min_index = index
        for j in range(index, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[index] = arr[index], arr[min_index]
        index += 1
    print(arr)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        num = arr[i]
        for j in range(i - 1, -1, -1):
            if num < arr[j]:
                arr[j + 1] = arr[j]
                arr[j] = num
    print(arr)


def shell_sort(arr):
    k = 5
    for i in range(k, -1, -2):
        for j in range(len(arr) - k):
            if arr[j] > arr[j + i]:
                arr[j], arr[j + i] = arr[j + 1], arr[j]
    print(arr)


def merge_sort(arr):
    if not arr: return []
    if len(arr) == 1: return arr
    length = len(arr)
    left = merge_sort(arr[:length // 2])
    right = merge_sort(arr[length // 2:])
    arr = merge_sort_core(left, right)
    return arr


def merge_sort_core(left, right):
    index_l, index_r = 0, 0
    ret = []
    while index_l < len(left) and index_r < len(right):
        if left[index_l] <= right[index_r]:
            ret.append(left[index_l])
            index_l += 1
        else:
            ret.append(right[index_r])
            index_r += 1
    if index_l == len(left):
        ret += right[index_r:]
    else:
        ret += left[index_l:]
    return ret


def quick_sort(arr, left, right):
    if left < right:
        pivot_index = partition(arr, left, right)
        quick_sort(arr, left, pivot_index)
        quick_sort(arr, pivot_index + 1, right)
    return arr


def partition(arr, left, right):
    pivot = left
    index = left + 1
    for i in range(index, right):
        if arr[i] <= arr[pivot]:
            arr[i], arr[index] = arr[index], arr[i]
            index += 1
    arr[pivot], arr[index - 1] = arr[index - 1], arr[pivot]
    return index - 1


def heap_sort(arr):
    for i in range(len(arr)//2-1, -1, -1):
        heap_adjust(arr, i, len(arr))
    for i in range(len(arr)-1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heap_adjust(arr, 0, i)
    return arr


def heap_adjust(arr, index, length):
    cur = arr[index]
    i = 2 * index + 1
    while i < length:
        if i + 1 < length and arr[i] < arr[i + 1]:
            i += 1
        if arr[i] > cur:
            arr[index] = arr[i]
            index = i
        else:
            break
        i = 2 * i + 1
    arr[index] = cur


def radix_sort(arr):
    counter = [[] for i in range(10)]
    mod = 10
    dev = 1
    maxdigit = 2
    for i in range(0, maxdigit):
        # 分配
        for j in range(0, len(arr)):
            bucket = arr[j] % mod // dev
            counter[bucket].append(arr[j])
        pos = 0
        # 收集
        for j in range(0, len(counter)):
            if counter[j] != None:
                while len(counter[j]) != 0:
                    arr[pos] = counter[j].pop(0)
                    pos += 1
        mod *= 10
        dev *= 10
    return arr


def counting_sort(arr):
    max_value = - sys.maxsize - 1
    min_value = sys.maxsize
    for i in range(len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
        if arr[i] < min_value:
            min_value = arr[i]
    ret = [0] * (max_value - min_value + 1)
    for i in range(len(arr)):
        ret[arr[i] - min_value] += 1
    index = 0
    for i in range(len(ret)):
        for j in range(ret[i]):
            arr[index] = i + min_value
            index += 1
    return arr


def bucket_sort(arr):
    # calculate max value and min value
    max_value = - sys.maxsize - 1
    min_value = sys.maxsize
    for i in range(len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
        if arr[i] < min_value:
            min_value = arr[i]
    # calculate the bucket nums
    bucket_num = (max_value - min_value) // 10 + 1
    buckets = [[] for i in range(bucket_num)]
    # put each elements into buckets
    for i in range(len(arr)):
        buckets[(arr[i]-min_value)//10].append(arr[i])
    # sort each bucket
    for i in range(len(buckets)):
        buckets[i] = quick_sort(buckets[i], 0, len(buckets[i]))
    # fill the origin array
    index = 0
    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            arr[index] = buckets[i][j]
            index += 1
    return arr



a = [12, 3, 2, 5, 6, 7, 2, 1, 4, 6, 87, 8, 2]
b = [2, 1, 3]
c = []
r = bucket_sort(a)
print(r)
