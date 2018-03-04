A = [0, 6, 3, 2, 7, 5, 4, 9, 1, 8]

print "Before sorting, A: ", A

for i in xrange(len(A)):
    is_sorted = True
    for j in xrange(len(A)-1, i, -1):
        if A[j] < A[j-1]:
            A[j-1], A[j] = A[j], A[j-1]
            is_sorted = False
    if is_sorted:
        break

print "After sorting, A: ", A
