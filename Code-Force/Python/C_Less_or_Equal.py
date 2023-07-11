def LessOrEqual(arr, k):
    arr.sort()
    answer = 0

    if k == 0:
        answer = arr[0] - 1
    elif k == 1 and len(arr) == 1:
        answer = arr[0] if arr[0] > 1 else -1
    elif k == len(arr):
        answer = arr.pop()    
    else:
        answer = -1 if arr[k-1] == arr[k] else arr[k] - 1
    return answer if answer in range(1, pow(10, 9) + 1) else -1

line = input().split(" ")
k = int(line[1])

arr = list(map(int, input().split(" ")))
print(LessOrEqual(arr, k))