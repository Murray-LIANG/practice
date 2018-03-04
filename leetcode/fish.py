import random


def coins_count():
    coins = []
    while coins[-4:] != [1] * 4:
        coins.append(random.randint(0, 1))
    return len(coins)


count = [coins_count() for _ in xrange(10000)]
print(count)
avg = [sum(count[:i + 1]) / (i + 1) for i in xrange(len(count))]
print(avg)
