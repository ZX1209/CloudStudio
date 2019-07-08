import math
from bisect import bisect_left
from pathlib import Path

# don't know if cwdPath always right
cwdPath = Path('.').resolve()
homePath = cwdPath.home()
#


def byteFormat(bytes):
    """byteFormat
    """
    return "".join("0x{:02x} ".format(letter) for letter in bytes)


def isChinese(w):
    """isChinese
    """
    if w >= u'\u4E00' and w <= u'\u9FA5':
        return True
    else:
        return False


def mold(x, y=None):
    """
    return sqrt(x**2+y**2)
    """
    if y is None:
        y = x[1]
        x = x[0]
    return math.sqrt(x**2 + y**2)


def vectorAngle(v1: [int, int], v2):
    angle = math.atan2(v1[1], v1[0]) - math.atan2(v2[1], v2[0])

    if angle > math.pi:
        angle -= 2 * math.pi
    elif angle < -math.pi:
        angle += 2 * math.pi

    return angle


def low_around(nums: list, target: int):
    nums.sort()
    for i, num in enumerate(nums):
        if num >= target:
            break
    return nums[i - 1], num


def low_around_index(nums: list, target: int):
    tmpnums = sorted(nums)
    for i, num in enumerate(tmpnums):
        if num >= target:
            break
    return nums.index(tmpnums[i - 1]), nums.index(num)


def high_around_index(nums: list, target: int):
    tmpnums = sorted(nums, reverse=True)
    for i, num in enumerate(tmpnums):
        if num <= target:
            break
    return nums.index(num), nums.index(tmpnums[i - 1])


def findSameElement(l1, l2):
    """找到两个数值列表中共同出现的数,可重复
    """
    ll = len(l1)
    rl = len(l2)
    li = 0
    ri = 0
    tmpSameY = []
    while li < ll and ri < rl:
        if l1[li] < l2[ri]:
            li += 1
        elif l1[li] > l2[ri]:
            ri += 1
        else:
            tmpSameY.append(l1[li])
            li += 1
            ri += 1
    return tmpSameY


# 2.83 µs ± 1.03 µs per loop (mean ± std. dev. of 7 runs, 100000 loops each)
def lower_bound(l, v):
    """bisect_left
    """
    return bisect_left(l, v)


# 867 ns ± 97.2 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
def binary_lower_bound(ol, v):
    """bisect_left
    """
    l = 0
    r = len(ol) - 1
    while l < r:
        mid = (l + r) // 2
        if v > ol[mid]:
            l = mid
        elif v <= ol[mid]:
            r = mid - 1
    return l


def binarySearch(ol, v):
    """bisect_left
    """
    l = 0
    r = len(ol) - 1
    while l < r:
        mid = (l + r) // 2
        if v > ol[mid]:
            l = mid + 1
        elif v < ol[mid]:
            r = mid - 1
        else:
            return mid
    return -1


char = str


def charMove(c: char, i: int) -> char:
    return chr(ord(c) + i)


def charMinus(c1: char, c2: char) -> int:
    return ord(c1) - ord(c2)


def indexAll(l, v):
    tmp = []
    i = 0
    while i < len(l):
        try:
            i = l.index(v, i)
            tmp.append(i)
        except ValueError:
            return tmp

        i += 1
    return tmp


def splitList(l, v):
    tmp = []
    tmpindex = indexAll(l, v)
    tmpindex = tmpindex

    tmp.append(l[:tmpindex[0]])

    i = 0
    while i < len(tmpindex) - 1:
        tmp.append(l[tmpindex[i] + 1:tmpindex[i + 1]])
        i += 1

    tmp.append(l[tmpindex[-1] + 1:])
    return tmp


def splitNum(n):
    ans = []
    while n > 0:
        ans.append(n % 10)
        n //= 10
    return ans


# 排列组合 C_n^m
def C(n, m):
    return math.factorial(n) // (math.factorial(n - m) * math.factorial(m))


# 因数分解
def Factorization(n):
    res = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            res.append(i)
            res.append(n // i)
    return res


def decToN(i, base):
    if i == 0:
        return "0"
    ans = []
    flag = 0

    if i < 0:
        flag = 1
        i = abs(i)

    while i > 0:
        ans.append(str(i % base))
        i //= 7

    if flag:
        ans.append('-')
    ans.reverse()

    return "".join(ans)


def is_primer(n):
    if n == 2 or n == 3:
        return 1

    if n % 6 != 1 and n % 6 != 5:
        return 0

    i = 5
    while i <= n**(1 / 2):
        if n % i == 0:
            return 0
        i += 1

    return 1


def rprimers(n):
    for i in range(2, n + 1):
        if is_primer(i):
            yield i


def rangePrimers(*args):
    """generator of range primers
    [start,end)
    rangePrimers(end)
    rangePrimers(start,end)
    """
    if len(args) == 1:
        start = 2
        end, = args  # args like (int,) not (int)
    elif len(args) == 2:
        start, end = args
    else:
        print("too many or too less args")
        start = 2
        end = 100

    for i in range(start, end):
        if is_primer(i):
            yield i


def howManyArgs(*args):
    print(len(args))
    print(args)


def nprimers(n):
    count = 0
    i = 2
    while count < n:
        if is_primer(i):
            yield i
            count += 1
        i += 1


# math


# 等差数列?
def Sn(a1, an, n, d=None):
    if d != None:
        n = 1 + (an - a1) / d

    return n * (a1 + an) / 2


# 等比数列
def Sq(a1, an, n, q=None):
    if q != None:
        n = 1 + (an - a1) / d

    return n * (a1 + an) / 2
