#!/bin/python3

import math
import os
import random
import re
import sys

subset_a = []
subset_b = []
sumA = 0
sumB = 0


def subset_a(arr):
    arr.sort()

    while arr:
        if sumA <= sumB:
            append_value_to_a(arr)
        else:
            is_last_num = len(arr) == 1
            checksum = sumB + arr[0] > sumA

            if is_last_num and checksum:
                append_value_to_a(arr)
            else:
                append_value_to_b(arr)

    subset_a.sort()

    return subset_a


def append_value_to_a(sorted_array):
    global sumA
    last_element = sorted_array.pop()
    subset_a.append(last_element)
    sumA += last_element


def append_value_to_b(sorted_array):
    global sumB
    first_element = sorted_array.pop(0)
    subset_b.append(first_element)
    sumB += first_element


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = subsetA(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
