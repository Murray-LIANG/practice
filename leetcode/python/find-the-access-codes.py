
def answer(l):

    sum_of_2 = []
    for i in range(0, len(l)):
        sum_of_2.append(sum(1 if l[i] % l[j] == 0 else 0 for j in range(0, i)))

    sum_of_3 = []
    for i in range(0, len(l)):
        sum_of_3.append(sum(sum_of_2[j] if l[i] % l[j] == 0 else 0 for j in range(0, i)))

    return sum(sum_of_3)


print(answer([1,3,4,5,6,12]))