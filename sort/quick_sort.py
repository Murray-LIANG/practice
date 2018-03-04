
def pivot(A):
    l, r = 0, len(A) - 1
    c = (l+r) / 2
    if A[l] > A[c]:
        A[l], A[c] = A[c], A[l]
    if A[l] > A[r]:
        A[l], A[r] = A[r], A[l]
    if A[c] > A[r]:
        A[c], A[r] = A[r], A[c]

    # A[l] < A[c] < A[r]
    A[c], A[r-1] = A[r-1], A[c]
    return A[r-1]

CUTOFF = 3

def quick_sort(A, l, r):

    if l + CUTOFF <= r:
        p = pivot(A)
        i, j = l + 1, r - 2
        while True:
            while A[i] < p:
                i += 1
            while A[j] > p:
                j -= 1
            if i < j:
                A[i], A[j] = A[j], A[i]
            else:
                break
        A[i], A[r-1] = A[r-1], A[i]

        quick_sort(A, 0, i-1)
        quick_sort(A, i+1, r)
    else:
        A.sort()

A = [0, 6, 3, 2, 7, 5, 4, 9, 1, 8]

print "Before sorting, A: ", A

quick_sort(A, 0, len(A)-1)

print "After sorting, A: ", A
