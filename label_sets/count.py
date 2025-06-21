import json
import torch


# 打开JSON文件
with open('/home/robot/swf/SimSeg/label_sets/pascal_context/top3.json', 'r') as file:
    # 解析JSON数据
    data = json.load(file)

# 初始化一个列表来存储每个字符串列表的数量
list_lengths = []

# 遍历JSON数据中的每个键值对
for key, value in data.items():
    # 检查值是否是列表类型
    if isinstance(value, list):
        # 计算列表的长度并添加到list_lengths列表中
        list_lengths.append(len(value))

# 打印每个字符串列表的数量
print(list_lengths)
