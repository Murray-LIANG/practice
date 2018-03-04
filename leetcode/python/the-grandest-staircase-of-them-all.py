"""
The problem needs you to calculate all the cases that N = sum(Xi).
Let N = 10, and the list 1,2,3,4,5,6,7,8,9, then choose any numbers from the
list to let sum of the numbers equal to 10. How many combination it is?

Use DP, it is similar with the backpack problem. Let dp(i,n) is the count of
combination of choosing number from [1...i] whose sum is n.
dp(i,n) = dp(i-1,n) + dp(i-1,n-i) while i = 1 -> n-1

Initially, dp(1,i) = 0 except dp(1,1) = 1
"""


def answer(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n):
        new_dp = [0] * (n + 1)
        for j in range(1, n + 1):
            new_dp[j] = dp[j]
            if j - i == 0:
                new_dp[j] += 1
            if j - i > 0:
                new_dp[j] += dp[j - i]
        dp = new_dp

    return dp[n]


print(answer(7))
print(answer(200))
