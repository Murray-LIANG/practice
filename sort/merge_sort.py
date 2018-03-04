
def merge_sort(A, start, end):
    if start < end:
        center = (start + end) / 2
        merge_sort(A, start, center)
        merge_sort(A, center+1, end)
        merge(A, start, center, end)

def merge(A, start, center, end):
    # left list is [start ... center]
    # right one is [center+1 ... end]
    l_start = start
    l_end = center
    r_start = center + 1
    r_end = end

    l_pos = l_start
    r_pos = r_start

    tmp = []
    while l_pos <= l_end and r_pos <= r_end:
        if A[l_pos] <= A[r_pos]:
            tmp.append(A[l_pos])
            l_pos += 1
        else:
            tmp.append(A[r_pos])
            r_pos += 1
    while l_pos <= l_end:
        tmp.append(A[l_pos])
        l_pos += 1
    while r_pos <= r_end:
        tmp.append(A[r_pos])
        r_pos += 1
    for i in xrange(start, end+1):
        A[i] = tmp.pop(0)

A = [24, 13, 26, 1, 2, 27, 38, 15]
print "Before sorting, A: ", A
merge_sort(A, 0, len(A)-1)
print "After sorting, A: ", A
