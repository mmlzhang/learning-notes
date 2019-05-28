
from mmap import mmap


def get_lines(file):
    with open(file, "rb") as f:
        for i in f:
            yield i


def get_lines2(file):
    with open(file, "r+") as f:
        m = mmap(f.fileno(), 0)
        tmp = 0
        for i, char in enumerate(m):
            if char == b"\n":
                yield m[tmp: i + 1].decode()
                tmp = i + 1


def print_directory_contents(path):
    """
    这个函数接收文件夹的名称作为输入参数
    返回该文件夹中文件的路径
    以及其包含文件夹中文件的路径
    """
    import os
    for s_child in os.listdir(path):
        s_c_path = os.path.join(path, s_child)
        if os.path.isdir(s_c_path):
            print_directory_contents(s_c_path)
        else:
            print(s_c_path)


def day_of_year(year, month, day):
    """输入日期， 判断这一天是这一年的第几天"""
    import datetime
    now_date = datetime.date(year=int(year), month=int(month), day=day)
    begin_date = datetime.date(year=year, month=1, day=1)
    return (now_date - begin_date).days + 1


def shuffle_list(alist):
    """打乱一个排好序的list对象alist"""
    import random
    return random.shuffle(alist)


def sorted_dict_value(adict):
    """现有字典 d= {'a':24,'g':52,'i':12,'k':33}请按value值进行排序"""
    return sorted(adict.items(), key=lambda x: x[1])


def reverse_str(astr):
    """字符串反转"""
    return astr[::-1]


def different_elem(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    print(set1 & set2)
    print(set1 ^ set2)


from typing import List
Vector = List[float]


def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]


def reverse_num(num):
    """反转整数"""
    if -10 < num < 10:
        return num
    str_num = str(num)
    if str_num[0] != "-":
        str_reverse = str_num[::-1]
        result = int(str_reverse)
    else:
        str_reverse = str_num[1:][::-1]
        result = -int(str_reverse)
    return result


import os


def get_files(dir, suffix):
    res = []
    for root, dirs, files in os.walk(dir):
        for filename in files:
            name, suf = os.path.splitext(filename)
            if suf == suffix:
                res.append(os.path.join(root, filename))
    print(res)


def get_files2():

    def pick(filename):
        if filename.endswith(".pyc"):
            print(filename)

    def scan_path(path):
        file_list = os.listdir(path)
        for obj in file_list:
            if os.path.isfile(obj):
                pick(obj)
            elif os.path.isdir(obj):
                scan_path(obj)


from glob import iglob


def get_files3(fp, postfix):
    for i in iglob(f"{fp}/**/*{postfix}", recursive=True):
        print(i)


def delete_elem(alist: list):
    for i in alist[:]:
        if i > 5:
            pass
        else:
            alist.remove(i)

    def del2():
        return filter(lambda x: x > 5, alist)

    def del3():
        return [i for i in alist if i > 5]


def get_missing_letter(a):
    s1 = set("".join(map(chr, range(ord("a"), ord("z") + 1))))
    s2 = set(a.lower())
    ret = "".join(sorted(s1 - s2))
    return ret


from functools import reduce


num = reduce(lambda x, y: x + y, [1, 2, 3])
print(num)


def atoi(s):
    num = 0
    for v in s:
        for j in range(10):
            if v == str(j):
                num = num * 10 + j
    return num


def atoi2(s):
    num = 0
    for v in s:
        num = num * 10 + ord(v) - ord("0")
    return num


def atoi3(s):
    num = 0
    for v in s:
        t = "%s * 1" % v
        n = eval(t)
        num = num * 10 + n


def atoi4(s):
    return reduce(lambda num, v: num * 10 + ord(v) - ord("0"), s, 0)


def two_sum(nums, target):
    """
    给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
    示例:给定nums = [2,7,11,15],target=9 因为 nums[0]+nums[1] = 2+7 =9,所以返回[0,1]
    :param nums: List[int]
    :param target: int
    """
    d = {}
    size = 0
    while size < len(nums):
        if target - nums[size] < size:
            return [d[target - nums[size]], size]
        else:
            d[nums[size]] = size
        size += 1


alist = []
alist_sort = sorted(alist, key=lambda x: x.get("age"), reverse=True)


def num_list(num):
    return num


import re

# .统计一个文本中单词频次最高的10个单词

def top_10(filepath):

    distone = {}
    with open(filepath) as f:
        for line in f:
            line = re.sub("\W+", " ", line)
            lineone = line.split()
            for keyone in lineone:
                if not distone.get(keyone):
                    distone[keyone] = 1
                else:
                    distone[keyone] += 1
    num_ten = sorted(distone.items(), key=lambda x: x[1], reverse=True)[:10]
    num_ten = [x[0] for x in num_ten]
    return num_ten


from collections import Counter


def top_10_2(f):
    with open(f) as f:
        return list(map(lambda c: c[0], Counter(re.sub("\W+", " ", f.read()).split()).most_common(10)))


# 两个有序列表，l1,l2，对这两个列表进行合并不可使用extend


def loop_merge_sort(l1, l2):
    tmp = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l1[0])
            del l1[0]
    while len(l1) > 0:
        tmp.append(l1[0])
        del l1[0]
    while len(l2) > 0:
        tmp.append(l2[0])
        del l2[0]
    return tmp


# 让所有奇数都在偶数前面，而且奇数升序排列，偶数降序排序，如字符串'1982376455',变成'1355798642'


def func1(l):
    if isinstance(l, str):
        l = [int(i) for i in l]
    l.sort(reverse=True)
    for i in range(len(l)):
        if l[i] % 2 > 0:
            l.insert(0, l.pop(i))
    print("".join(str(e) for e in l))


def second_bigger(num_list):
    tmp_list = sorted(num_list)
    print(tmp_list[-2])

    # 2
    one = num_list[0]
    two = num_list[0]
    for i in range(1, len(num_list)):
        if num_list[i] > one:
            two = one
            one = num_list[i]
        elif num_list[i] > two:
            two = num_list[i]

    # 3
    from functools import reduce
    num = reduce(lambda ot, x: ot[1] < x and (ot[1], x) or ot[0] < x and (x, ot[1]) or ot, num_list, (0, 0))[0]
    return print("reduce: ", num)


def multi():
    return [lambda x: i * x for i in range(4)]


print([m(3) for m in multi()])

from functools import wraps

if __name__ == '__main__':
    list1 = [1, 2, 34, 4]
    list2 = [2, 3, 4, 6, 8]
    different_elem(list1, list2)


