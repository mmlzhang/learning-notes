
import re

# 请写出一段代码用正则匹配出ip
s = 'kkk 192.168_1.136 k111kk 192.168.1.137 kk 192.168.1.138 kk'
res = re.findall(r"\d+\.\d+\.\d+\.\d+", s)
print(res)


a = "abbbbbbbbbcccccccccc"
print(re.sub(r"b+", "b", a))

print(a.find("b"))

pa = r"^\w+.*\d+$"
s = "asdfs$##   2324asdasd```121"
print(re.findall(pa, s))


# 怎么过滤评论中的表情
def filter_emoji(desstr, restr):
    try:
        co = re.compile(u"[\U00010000-\U0010ffff]")
    except re.error:
        co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    return co.sub(restr, desstr)


