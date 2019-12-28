class Sleigh(object):
    def authenticate(self, name, password):
        return(name == 'Santa Claus' and password == 'Ho Ho Ho!')
    
test = Sleigh()

test.authenticate('bob', 'myers')

def is_nice(arr):
    return min([a + 1 in arr or a - 1 in arr for a in set(arr)]) and arr

arr = [3,4,5,7]

odd = [4,5,6,8]

is_nice(arr)

import numpy as np

def find_outlier(integers):
    integers = np.array(integers)
    
    is_even = np.array([i % 2 == 0 for i in integers])
    
    if sum(is_even) == 1:
        return(int(integers[is_even]))
    else:
        return(int(integers[~is_even]))

find_outlier(odd)

def find_outlier(integers):
    
    is_even = [i for i in integers if i % 2 == 0]
    is_odd = [i for i in integers if i % 2 != 0]
    
    return(is_even[0] if len(is_even) == 1 else is_odd[0])

find_outlier(odd)
find_outlier(arr)

import itertools
def two_sum(numbers, target):
    numbers.sort()
    pairs = list(itertools.combinations(numbers, 2))
    idx = [
        (
            numbers.index(i[0]),
            numbers.index(i[1]) if numbers.index(i[0]) != numbers.index(i[1]) else numbers.index(i[1]) + 1
        ) for i in pairs if sum(i) == target
    ][0]
    return(idx)

numbers = [1, 2, 3]
target = 4

two_sum(numbers, target)

test_arr = [1234,5678,9012]
test_res = 14690

two_sum(test_arr, test_res)

numbers = [2,2,3]
target = 4

two_sum(numbers, target)

numbers[-numbers.index(i[0])].index(i[1])

i = (2, 2)
numbers[numbers.index(i[0])+1:]






def two_sum(numbers, target):
    for i, n in enumerate(numbers):
        for j, m in enumerate(numbers):
            if n + m == target and i != j:
                return (i, j) 


def two_sum(numbers, target):
    return list((i, j) for i, n in enumerate(numbers) for j, m in enumerate(numbers) if n + m == target and i != j)[0]






