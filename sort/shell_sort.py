A = [81, 94, 11, 96, 12, 35, 17, 95, 28, 58, 41, 75, 15]

delta = len(A) / 2

print "Before sorting, A: ", A
while delta > 0:
    for i in xrange(delta, len(A)):
        tmp = A[i]
        for j in xrange(i, delta-1, -delta):
            if A[j-delta] > tmp:
                A[j] = A[j-delta]
            else:
                A[j] = tmp
                break
        else:
            A[j-delta] = tmp
    delta /= 2
print "After sorting, A: ", A

