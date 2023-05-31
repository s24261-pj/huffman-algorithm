def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def min_heapify(array, i, heap_size):
    l = left(i)
    r = right(i)

    if l <= heap_size and array[l].frequency < array[i].frequency:
        least = l
    else:
        least = i

    if r <= heap_size and array[r].frequency < array[least].frequency:
        least = r

    if least != i:
        array[i], array[least] = array[least], array[i]
        min_heapify(array, least, heap_size)


def build_min_heap(array):
    heap_size = len(array) - 1

    for i in range(len(array) // 2 - 1, -1, -1):
        min_heapify(array, i, heap_size)


def get_min(array):
    min_value = array[0]
    array[0] = array[-1]
    array.pop()
    min_heapify(array, 0, len(array) - 1)

    return min_value


def insert(array, value):
    array.append(value)
    i = len(array) - 1

    while i > 0 and array[i].frequency < array[(i - 1) // 2].frequency:
        array[i], array[(i - 1) // 2] = array[(i - 1) // 2], array[i]
        i = (i - 1) // 2

    return array
