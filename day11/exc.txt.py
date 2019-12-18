# """
# 练习:编辑一个函数,
#     传入端口名称,
#     返回这个端口描述信息中,
#     对应的address的值
# """
#
# import re
# def get_address(port):
#     f= open("esc.txt")
#     while True:
#         #搞到每一段
#         data = ""
#         for line in f :
#             if line == "\n":
#                 break
#             data += line
#             #文件结尾
#         if not data:
#             return
#         obj = re.match(r"\s+".data)
#         if port == obj.group():
#         #找到目标段
#             pattern = r"[0-9]"
# if '__main__':