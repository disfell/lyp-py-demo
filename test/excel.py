import pandas as pd

# 读取TXT文件内容
with open('output.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 初始化字段名和描述的列表
index_names = []
descriptions = []

# 遍历每一行，分割字段名和描述
for line in lines:
    if line.strip():  # 确保不处理空行
        name, desc = line.split(", ", 1)  # 分割前，先去除每行首尾的空白字符
        index_names.append(name)
        descriptions.append(desc.strip())  # 去除描述两端的空白字符

# 使用列表创建一个MultiIndex
index = pd.MultiIndex.from_arrays([index_names, descriptions], names=['字段名', '描述'])

# 创建一个空的DataFrame，并指定行索引
df = pd.DataFrame(index=index)

# 写入Excel文件
df.to_excel('output_vertical.xlsx', index=True, header=False, engine='openpyxl')

# 打印完成信息
print("数据已导出到Excel文件，并且是竖向输出。")