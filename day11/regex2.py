"""
match对象说明
"""
import re

pattern = r'(ab)cd(?P<pig>ef)'
regex = re.compile(pattern)
obj = regex.search("abcdefgh123", 0, 9)  # match对象

# 属性变量
print(obj.pos)  # 目标字符串开始位置
print(obj.endpos)  # 目标字符串结束位置
print(obj.lastgroup)  # 最后一组名
print(obj.lastindex)  # 最后一组序号

print("==============================")
# 属性方法
print(obj.span())  # 匹配内容的起止位置
print(obj.start())  # s[start():end()]
print(obj.end())
print(obj.groupdict())  # 捕获组字典
print(obj.groups())  # 子组对应内容
print(obj.group())  # match对象对应内容
print(obj.group(1))
print(obj.group('pig'))
