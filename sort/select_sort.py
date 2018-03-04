A = [0, 6, 3, 2, 7, 5, 4, 9, 1, 8]

print "Before sorting, A: ", A

for i in xrange(0, len(A)):
    min_index = i 
    for j in xrange(i+1, len(A)):
        if A[j] < A[min_index]:
            min_index = j
    A[i], A[min_index] = A[min_index], A[i]

print "After sorting, A: ", A

