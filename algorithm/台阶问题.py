
fib = lambda n: n if n <= 2 else fib(n - 1) + fib(n - 2)

print(fib(5))


def memo(func):
    cache = {}

    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


@memo
def fib2(n):
    if n < 2:
        return 1
    return fib2(n - 1) + fib2(n - 2)


print(fib2(5))


def fib3(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return b


print(fib3(5))


def get_value(l, r, c):
    return l[r][c]


def find(l, x):
    m = len(l) - 1
    n = len(l[0]) - 1
    r = 0
    c = n

    while c >= 0 and r <= m:
        value = get_value(l, r, c)
        if value == x:
            return True
        elif value > x:
            c = c - 1
        elif value < x:
            r = r + 1
    return False


l1 = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4]
l2 = {}.fromkeys(l1).keys()
print(list(l2))


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def swap_pairs(self, head):
        if head and head.next:
            next = head.next
            head.next = self.swap_pairs(next.next)
            next.next = head
            return next
        return head


a = (1, 2, 3)
b = (2, 3, 4)
print(dict(zip(a, b)))


def _recursion_merge_sort2(l1, l2, tmp):

    if len(l1) == 0 or len(l2) == 0:
        tmp.extend(l1)
        tmp.extend(l2)
        return tmp
    else:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
        return _recursion_merge_sort2(l1, l2, tmp)


def recursion_merge_sort2(l1, l2):
    return _recursion_merge_sort2(l1, l2, [])


l1 = [1, 2, 3, 4, 5]
l2 = [2, 4, 6, 8]

res = recursion_merge_sort2(l1, l2)
print(res)


