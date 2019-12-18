"""
flags 功能扩展示例
"""
import re

s = """Hello
北京
"""
# 只匹配ascii
# regex = re.compile(r'\w+',flags=re.A)

# 不区分大小写
# regex=re.compile(r'[a-z]+',flags=re.I)

# . 可以匹配换行
# regex = re.compile(".+",flags=re.S)

# ^ $ 匹配每行开头结尾位置
regex = re.compile("^\w+", flags=re.M)

l = regex.findall(s)
print(l)
