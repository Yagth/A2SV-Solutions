#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    def printArr(arr):
        printArr = [str(a) for a in arr ]
        temp = " ".join(printArr)
        print(temp)
    # Write your code here
    e = arr[n-1]
    j = n - 2
    temp = arr[j]
    while temp >= e and j >= 0:
        arr[j+1] = temp
        j -= 1
        temp = arr[j]
        printArr(arr)
        
    arr[j+1] = e
    printArr(arr)
            
        
        
            
            
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
