import json

# 读取JSON文件
with open('/home/robot/swf/SimSeg/label_sets/pascal_voc/top1.json', 'r') as file:
    data = json.load(file)

# 遍历JSON数据，为每个key添加其对应value的第一个值
for key, values in data.items():
    values.insert(0, key)

# # 遍历 JSON 数据, 将每个键的所有值都替换为该键的第一个值
# for key in data:
#     first_value = data[key][0]
#     data[key] = [first_value] * len(data[key])
# 将更新后的数据保存回JSON文件
with open('/home/robot/swf/SimSeg/label_sets/pascal_voc/top1_super.json', 'w') as file:
    json.dump(data, file, indent=4)
