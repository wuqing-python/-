"""

"""
import re

s = "今年是2019年12月10日," \
    "2019年的愿望那个实现了么," \
    "保持95斤你实现了没"

pattern = r'\d+'
# 获取匹配内容的迭代器
result = re.finditer(pattern, s)
for i in result:
    print(i.group())

# 完全匹配
obj = re.fullmatch('.+', s)

#不区分大小写
s="""hello
        北京"""

print(obj.group())

# 匹配开始位置
obj = re.match('\w+', s)
print(obj.group())

# 匹配第一处
obj = re.search('\d+', s)
print(obj.group())
