info = [
    ("张三", {"math":80, "english":90}),
    ("李四", {"math":88, "english":76}),
    ("张三", {"math":92, "english":81})
]
name_set = set()
total_dict = {}
for name, score in info:
    name_set.add(name)
    total = score["math"] + score["english"]
    print(name, total)
    total_dict[name] = total
print("去重姓名：", name_set)
print("总分字典：", total_dict)
