# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 11:30:02 2018

@author: wigr11ab
"""


def compareTriplets(a, b):
    sumA, sumB = 0, 0
    for i in range(len(a)):
        if a[i] > b[i]:
            sumA +=1
        elif a[i] < b[i]:
            sumB += 1
    return [sumA, sumB]

a = [4, 5, 8]
b = [3, 2, 9]

sumA = sum([1 for i in range(len(a)) if a[i] > b[i]])
sumB = sum([1 for i in range(len(a)) if a[i] < b[i]])

compareTriplets(a, b)

matrix = [[1,2,3],
          [4,5,6],
          [9,8,9]]

len(matrix)
squares = [(i + 1) ** 2 for i in range(len(matrix))]

pos_diag = sum([matrix[i][i] for i in range(len(matrix))])
neg_diag = sum([matrix[len(matrix) - (1 + i)][i] for i in range(len(matrix))])

arr = [1, 3, 5, 7, 9]

def plusMinus(arr):
    neg = sum(i < 0 for i in arr) / len(arr)
    neu = sum(i > 0 for i in arr) / len(arr)
    pos = sum(i == 0 for i in arr)/ len(arr)
    return "{:.6f}".format(neg)

plusMinus(arr)

def staircase(n):
    for i in range(1, n + 1):
        print(" "*(n - i)+"#"*i)

staircase(6)

arr = [1, 3, 5, 7, 9]

def miniMaxSum(arr):
    mini = sum(arr) - max(arr)
    maxi  = sum(arr) - min(arr)
    print('{}{}{}'.format(mini, " ", maxi))

miniMaxSum(arr)

candles = [3,2,1,3]

def birthdayCakeCandles(candles):
    print(candles.count(max(candles)))

birthdayCakeCandles(candles)

s = "07:05:45PM"
t = "07:05:45AM"
v = "12:05:45PM"
w = "12:05:45AM"

def timeConversion(s):
    if s[len(s) - 2:] == 'PM':
        s = str(int(s[:2]) + 12) + s[2:] if int(s[:2]) < 12 else "12" + s[2:]
    else:
        s = s if int(s[:2]) < 12 else "00" + s[2:]
    return s[:len(s) - 2]

timeConversion(s)
timeConversion(t)
timeConversion(v)
timeConversion(w)

A = [1,2,2,1]
B = [3,1,1,2]

k = 3
test = [A[i] + B[i] - k for i in range(len(A))]

def twoArrays(k, A, B):
    A.sort(reverse = False)
    B.sort(reverse = True)
    pos = [A[i] + B[i] - k for i in range(len(A))]
    return 'YES' if min(pos) >= 0 else 'NO'

twoArrays(k, A, B)

def gradingStudents(grade):
    for i in grade:
        idx = grade.index(i)
        if i % 5 >= 3 and i >= 38:
            grade[idx] = i + 5 - i % 5 
    return grade

grade = [73, 67, 38, 33]

gradingStudents(grade)

def countApplesAndOranges(s, t, a, b, apples, oranges):
    print(sum(1 for i in apples  if i + a in range(s, t + 1)))
    print(sum(1 for i in oranges if i + b in range(s, t + 1)))

s, t, a, b = 7, 11, 5, 15

apples  = [-2, 2, 1]
oranges = [5, -6]

countApplesAndOranges(s, t, a, b, apples, oranges)

def kangaroo(x1, v1, x2, v2):
    if x1 < x2 and v1 > v2:
        return 'YES' if (x2 - x1) / (v1 - v2) % 1 == 0 else 'NO'
    if x2 < x1 and v2 > v1:
        return 'YES' if (x1 - x2) / (v2 - v1) % 1 == 0 else 'NO'
    return 'NO'    

x1, v1, x2, v2 = 0, 3, 4, 2

kangaroo(x1, v1, x2, v2)


a = [2, 4]
b = [16, 32, 96]

def getTotalX(a, b):
    return sum(1 for i in range(1, int(min(b) / max(a)) + 1) \
    if not sum([k % (i * max(a)) for k in b] + [i * max(a) % k for k in a]))

getTotalX(a, b)

a = [3, 4]
b = [24, 48]

getTotalX(a, b)

def breakingRecords(scores):
    scores = list(scores)
    minBreaks = 0
    maxBreaks = 0
    minScore = scores[0]
    maxScore = scores[0]
    for i in scores[1:]:
        if i < minScore:
            minBreaks += 1
            minScore = i
        if i > maxScore:
            maxBreaks += 1
            maxScore = i
    print('{}{}{}'.format(maxBreaks, ' ', minBreaks))

scores = [3, 4, 21, 36, 10, 28, 35, 5, 24,42]

breakingRecords(scores)

s = [1, 2, 1, 3, 2]
t = [3, 2]
d = t[0]
m = t[1]

def birthday(s, d, m):
    arr  = [sum(i) for i in zip(s, s[1:])] if len(s) > 1 else s
    return sum((1 for s in arr if s == d))


birthday(s, d, m)

s = [4]
t = [4, 1]
d = t[0]
m = t[1]

birthday(s, d, m)

s = [1]*6
t = [3, 2]
d = t[0]
m = t[1]

birthday(s, d, m)

[i for i in zip(s, s[1:])]
[sum(s[i:i + m]) for i in range(len(s) - m + 1)] if len(s) > m - 1 else sum(s)


from itertools import combinations as combis
def divisibleSumPairs(n, k, ar):
    ar.sort()
    sums = [sum(i) for i in list(combis(ar, 2)) if sum(i) % k == 0] if len(ar) > 1 else 0
    return len(sums)


ar = [1, 3, 2, 6, 1, 2]
n = len(ar)
k = 3
divisibleSumPairs(n, k, ar)

arr = [1,4,4,4,5,3]
test = [arr.count(i) for i in arr]
arr.index(max(test))

def migratoryBirds(arr):
    count = [arr.count(i) for i in set(arr)]
    return list(set(arr))[count.index(max(count))]

arr = [1,4,4,4,5,3]
migratoryBirds(arr)

arr = [1,2,3,4,5,4,3,2,1,3,4]
migratoryBirds(arr)

arr = [3] * 10 ** 5 + [2] * 10 ** 5
migratoryBirds(arr)

def bonAppetit(bill, k, b):
    split = int(sum(bill[:k] + bill[k +1:]) / 2)
    print('Bon Appetit') if split == b else print(b - split)

bill = [3, 10, 2, 9]
k = 1
b = 12
bonAppetit(bill, k, b)

bill = [3, 10, 2, 9]
k = 1
b = 7
bonAppetit(bill, k, b)

from itertools import combinations as combis
ar.sort()
st = list(set(ar))
count = [ar.count(i) for i in st]
mod   = [i / 2 if i % 2 == 0 else (i - 1) / 2 for i in count]

def sockMerchant(n, ar):
    uniques = list(set(ar))
    count   = [ar.count(i) for i in st]
    pairs   = int(sum([i / 2 if i % 2 == 0 else (i - 1) / 2 for i in count]))
    print(pairs)

n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
sockMerchant(n, ar)

def pageCount(n, p):
    if n / 2 >= p:
        return int(p / 2) if p % 2 == 0 else int((p - 1) / 2)
    else:
        if n % 2 == 0:
            return int((n - p) / 2) if (n - p) % 2 == 0 else int((n - p + 1) / 2)
        else:
            return int((n - p) / 2) if (n - p) % 2 == 0 else int((n - p - 1) / 2)

n = 18
p = 9
pageCount(n, p)

n = 15
p = 7
pageCount(n, p)

def catAndMouse(x, y, z):
    if abs(z - x) == abs(z - y):
        return 'Mouse C'
    else:
        return 'Cat A' if abs(z - x) < abs(z - y) else 'Cat B'

x, y, z = 1, 2, 3 # Cat A, Cat B, Mouse C
catAndMouse(x, y, z)

x, y, z = 1, 3, 2
catAndMouse(x, y, z)

height = [1,2,3,3,2]
k = 1

def hurdleRace(k, height):
    return max(max(height) - k, 0)

hurdleRace(k, height)

def utopianTree(n):
    if n == 0:
        return 1

n = 4
utopianTree(n)

n = 1
utopianTree(n)
    
"test = [h[(ord(i) - 97)] for i in word]"

def designerPdfViewer(h, word):
    return max([h[(ord(i) - 97)] for i in word]) * len(word)


h = [1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
word = 'abc'
designerPdfViewer(h, word)

h = [1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,7]
word = 'zaba'
designerPdfViewer(h, word)

def angryProfessor(k, a):
    onTime = sum([1 for i in a if i <= 0])
    return 'YES' if onTime < k else 'NO'

a = [-1,-1,0,0,1,1]
k = 4
angryProfessor(k, a)



def findDigits(n):
    ints = [int(i) for i in str(n) if i != '0']
    return sum([1 for i in ints if n % i == 0])

n = 12
n = 1012
sum([1 for i in str(n) if n % int(i) == 0])

n = 3
recs = 5
liks = (recs - recs % 2) / 2
for i in range(1,n):
    recs  = (recs - recs % 2) / 2 * 3
    liks += (recs - recs % 2) / 2

test = [(a.count(i), a.count(i+1)) for i in set(a)]
b = set(a)

[i + j for i, j in zip(a, b)]

def pickingNumbers(a):
    return max([sum((a.count(i), a.count(i+1))) for i in set(a)])

a = [1,2,2,3,1,2]
pickingNumbers(a)

a = [4,6,5,3,3,1]
pickingNumbers(a)

def jumpingOnClouds(c):
    idx = 0
    jmp = 0
    while idx < len(c) - 2:
        idx += 2 if c[idx + 2] == 0 else 1
        jmp += 1
    return jmp if idx == len(c) - 1 else jmp + 1
    


c = [0,0,0,0,1,0]
jumpingOnClouds(c)

c = [0,0,1,0,0,1,0]
jumpingOnClouds(c)


k = 3
c = [1,1,1,0,1,1,0,0,0,0]
idx = 0
e = 100
while idx < len(c):
    idx += k
    e -= 1 if c[idx % len(c)] == 0 else 3

bool(idx)
not 8 % 8


def jumpingOnCloudsRev(c, k):
    idx = 0
    e   = 100
    while not (not idx % len(c) and idx):
        idx += k
        e   -= 1 if c[idx % len(c)] == 0 else 3
    return e


def cutTheSticks(arr):



arr = [1,2,3,4,3,3,2,1]
length = []
while bool(arr):
    length.append(len(arr))
    arr = [i - min(arr) for i in arr if i - min(arr)]


arr = [3,3,2,1,3]
[arr.count(i) for i in set(arr)]

[i for i in enumerate(arr) if list(set(arr)).count(i) > 1]