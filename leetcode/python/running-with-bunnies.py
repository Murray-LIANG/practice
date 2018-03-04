"""
Use a tuple `picked_bunnies` to store the bunnies picked up. That is, for 5
bunnies, (0,1,0,0,0) means only pick up the bunny #1. Besides, use a dict
`visited` to store the maximal time left after picking up the bunnies. That is,
visited[(0,1,0,0,0)] = 3 means after picking bunny #1 we still have 3 units
time.
Then use dfs to traverse the `times`. Once reach the bulkhead, we write down
the `visited` for current `picked_bunnies`. If it is better than previous one,
then update the answer.

When to stop the dfs? Because we only do the dfs when the left time is more
than current one in `visited`. The branch will be cut off if not. So we will
meet the end.
"""


def answer(times, time_limit):
    res = [[]]
    dfs_2(times, 0, {}, [0] * (len(times) - 2), time_limit, res)
    return res[0]


def dfs(times, row, visited, picked_bunnies, left_time, res):
    picked_bunnies = picked_bunnies[:]
    if row == len(times) - 1:
        if left_time >= 0 and sum(picked_bunnies) > len(res[0]):
            res[0] = [index for index, val in enumerate(picked_bunnies)
                      if val == 1]

    elif row > 0:
        picked_bunnies[row - 1] = 1

    t = ''.join(str(i) for i in picked_bunnies + [row])
    if t not in visited or visited[t] < left_time:
        visited[t] = left_time
        for next, n_time in enumerate(times[row]):
            if next == row:
                continue
            dfs(times, next, visited, picked_bunnies, left_time - n_time, res)


def dfs_2(times, row, visited, picked_bunnies, left_time, res):
    if row == len(times) - 1:
        if left_time >= 0 and sum(picked_bunnies) > len(res[0]):
            res[0] = [index for index, val in enumerate(picked_bunnies)
                      if val == 1]
    t = tuple(picked_bunnies + [row])
    if t in visited and visited[t] >= left_time:
        return

    visited[t] = left_time
    for next, n_time in enumerate(times[row]):
        if next == row:
            continue

        if 0 < next < len(times) - 1:
            picked_bunnies[row - 1] = 1
        dfs_2(times, next, visited, picked_bunnies, left_time - n_time, res)
        if 0 < next < len(times) - 1:
            picked_bunnies[row - 1] = 0


print(answer(
    [[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1],
     [9, 3, 2, 2, 0]],
    1))
print(answer(
    [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1],
     [1, 1, 1, 1, 0]],
    3))
# (int list) [0, 1]

print(answer(
    [[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1],
     [9, 3, 2, 2, 0]],
    1))
# (int list) [1, 2]
