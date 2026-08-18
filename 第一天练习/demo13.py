from pydoc import text

import elis

text=input("请输入一段文字：")
Z=z=s=k=0
for i in text:
    if i.isupper():
        Z=Z+1
    elif i.islower():
        z=z+1
    elif i.isdigit():
        s=s+1
    elif i==" ":
        k=k+1
print(f"大写字母{Z}个")
print(f"小写字母{z}个")
print(f"数字{s}个")
print(f"空格{k}个")
