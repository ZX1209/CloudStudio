import random


# [start,end] char
def randomChar(start=97, end=122):
    return chr(random.randint(start, end))


def randomStr():
    r = []
    for i in range(random.randint(3, 5)):
        r.append(randomChar())
    return "".join(r)


def randomDic(num=5):
    rdic = {}
    for i in range(num):
        rdic["key-" + randomStr()] = "value-" + randomStr()
    return rdic


def randomList(length=5):
    return [random.randint(0, 100) for i in range(length)]


def randomInts(length=100, start=0, end=100):
    yield random.randit(start, end)


def randomWhat(lists=None, appends=None):
    """for decide what to do
    lists:str    use lists for choice
    appends:str    use default list for choice but append others
    """
    L = lists if lists else ['Movie', 'Music', 'Game', 'Book', 'again']
    if appends:
        L.extend(appends)

    return random.choices(L)
