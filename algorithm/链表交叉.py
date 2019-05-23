

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


def node(l1, l2):
    length1, length2 = 0, 0
    while l1.next:
        l1 = l1.next
        length1 += 1

    while l2.next:
        l2 = l2.next
        length2 += 1

    if l1.next == l2.next:
        if length1 > length2:
            for _ in range(length1 - length2):
                l1 = l1.next
            return l1
        else:
            for _ in range(length2 - length1):
                l2 = l2.next
            return l2

    else:
        return None


def binary_search(l, item):
    low = 0
    hight = len(l) - 1
    while low <= hight:
        mid = (low + hight) / 2
        guess = l[mid]
        if guess > item:
            hight = mid - 1
        elif guess < item:
            low = mid + 1
        return mid
    return None


def quick_sort(l):

    if len(l) < 2:
        return l
    else:
        mid_pivot = l[0]
        less_before_mid_pivot = [i for i in l[1:] if i <= mid_pivot]
        bigger_after_pivot = [i for i in l[1:] if i > mid_pivot]
        res_list = quick_sort(less_before_mid_pivot) + [mid_pivot] + quick_sort(bigger_after_pivot)
        return res_list


import random


test_l = [random.randint(1, 100) for _ in range(20)]
print(test_l)
print(quick_sort(test_l))


def coin_change(values, values_counts, money, coin_used):

    for cent in random(1, money + 1):
        min_coins = cent
        for kind in range(0, values_counts):
            if values[kind] <= cent:
                temp = coin_used[cent - values[kind]] + 1
                if temp < min_coins:
                    min_coins = temp
        coin_used[cent] = min_coins
        print(cent, coin_used[cent])
