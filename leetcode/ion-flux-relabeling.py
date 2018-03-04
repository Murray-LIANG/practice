def answer(h, q):
    n = 2**h-1
    memo = [0] * n
    helper(1, n, memo)
    return [memo[each] for each in q]


def helper(start, end, memo):
    if start == end:
        return
    left, right = (end - start) // 2 + start - 1, end - 1
    memo[left] = memo[right] = end
    helper(start, left, memo)
    helper(left + 1, right, memo)


print(answer(5, [19, 14, 28]))
