A = [0, 6, 3, 2, 7, 5, 4, 9, 1, 8]

print "Before sorting, A: ", A
for i in xrange(2, len(A)):
    A[0] = A[i]
    for j in xrange(i-1, -1, -1):
        if A[j] > A[0]:
            A[j+1] = A[j]
        else:
            A[j+1] = A[0]
            break
            
print "After sorting, A: ", A
