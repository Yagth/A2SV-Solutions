def lexographicallySmaller(x):
    odd = 0
    even = 0
    for i in range(len(x)):
        if x[i] % 2 == 0:
            even += 1
        else: 
            odd += 1

    if odd and even:
        return sorted(x)
    else:
        return x
_ = input()
arr = list(map(int, input().split(" ")))
print(*lexographicallySmaller(arr))