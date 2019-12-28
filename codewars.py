# -*- coding: utf-8 -*-
"""
Created on Sun Dec 09 22:56:02 2018

@author: wigr11ab
"""
numbers = [7,8,3,4,5]

def removeSmallest(numbers):
    if len(numbers) == 0:
        return numbers
    idx = numbers.index(min(numbers))
    return [numbers[-i] for i in idx]

numbers = [1,2,0,3,0,5]
removeSmallest(numbers)

def to_camel_case(text):
    return text[0] + text.title()[1:].replace('_','').replace('-','') if text else text

text = 'the-stealth-warrior'
to_camel_case(text)

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

validate_pin('12456a')
validate_pin('124569')

test = "Dermatoglyphics"
[test.count(i) for i in test]

test1 = 'abA'
len(test1) == sum([test1.lower().count(i) for i in test1.lower()])

test = ''
len(test) == sum([test.lower().count(i) for i in test.lower()])

def is_isogram(string):
    return len(string) == sum([string.lower().count(i) for i in string.lower()])

def find_next_square(sq):
    return (sq ** .5 + 1) ** 2 if sq ** .5 % 1 == 0. else -1

find_next_square(121)
find_next_square(114)

testDumb = "2 4 6 8 10 11"

def iq_test(numbers):
    numbers = [int(i) for i in numbers.split(' ')]
    even = [i % 2 for i in numbers]
    return even.index(0) + 1 if sum(even) > 1 else even.index(1) + 1

iq_test(testDumb)

def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)

def countZeros(n):
    x = n // 5
    return x + countZeros(x) if x else 0

factorial(50)
countZeros(50)

test = 11

def solution(n):
    n = n - 1
    three = int((n - n % 3) / 3 + 1)
    five  = int((n - n % 5) / 5 + 1)
    subt  = int((n - n % 15) / 15 + 1 if n >= 15 else 0)
    threeSum = sum(3 * i for i in range(three))
    fiveSum  = sum(5 * i for i in range(five) )
    subSum   = sum(15* i for i in range(subt) )
    return threeSum + fiveSum - subSum

def solution2(n):
    return sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)

solution(950)
solution2(950)

customers = [10,12, 2,3,5]
customers = []
n = 2

def queue_time(customers, n):
    timeTaken = customers[:n]
    for i in customers[n:]:
        timeTaken[timeTaken.index(min(timeTaken))] += i
    return max(timeTaken) if timeTaken else 0

queue_time(customers, n)


from itertools import combinations as combis
def chooseBestSum(t, k, ls):
    travel  = [sum(i) for i in list(combis(ls, k))]
    return max( (s for s in travel if s <= t), default = None)

ls = [50, 55, 56, 57, 58]
t = 163
k = 3

chooseBestSum(t, k, ls)

ls = [91, 74, 73, 85, 73, 81, 87]
t = 230
k = 3

chooseBestSum(t, k, ls)

ls = [30, 40, 50, 60, 70, 80]
t  = 110
k  = 3

chooseBestSum(t, k, ls)

ls = [1,2,3,4,5,6]
t = 100
k = 3

chooseBestSum(t, k, ls)

def choose_best_sum(t, k, ls):
    return max((s for s in (sum(dists) for dists in combis(ls, k)) if s <= t), default=None)



lng  = 5
wdth = 4

mx = max(lng, wdth)
mn = min(lng, wdth)

a = []
while mn >= 1:
    a.append(mn)
    n = mx - mn
    mx = max(mn, n)
    mn = min(mn, n)

tt = lng * wdth
mx = max(lng, wdth)
mn = min(lng, wdth)
a = (mx - mx % mn) / mn
b = mx % mn * 1.0
c = mx * mn - (a * mn ** 2 + b ** 2)
