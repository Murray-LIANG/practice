def left_child(index):
    return 2*index


def perc_down(A, start, end):

    tmp = A[start]
    child = left_child(start)
    while child <= end:
        if child != end and A[child+1] > A[child]:
            child += 1
        if tmp < A[child]:
            A[start] = A[child]
            start = child
            child = left_child(start)
        else:
            break
    A[start] = tmp


A = [0, 31, 41, 59, 26, 53, 58, 97]

print "Before sorting, A: ", A

for i in xrange((len(A)-1)/2, 0, -1):
    perc_down(A, i, len(A)-1)

for i in xrange(len(A)-1, 0, -1):
    A[1], A[i] = A[i], A[1]
    perc_down(A, 1, i-1)

print "After sorting, A: ", A
