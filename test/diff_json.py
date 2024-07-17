from deepdiff import DeepDiff
import json


# 用于比较两个json文件的差异
def compare_json_detailed(json1, json2):
    diff = DeepDiff(json1, json2, ignore_order=True)
    return diff


def compare(file1, file2):
    # 加载两个JSON文件
    data1 = json.load(open(file1, 'r', encoding='utf-8'))
    data2 = json.load(open(file2, 'r', encoding='utf-8'))

    # 比较两个JSON文件的内容
    diff = compare_json_detailed(data1, data2)

    if diff:
        print("两个JSON文件内容不完全相同。")
        print("以下是不同的部分：")
        print(diff)
    else:
        print("两个JSON文件内容完全相同。")


if __name__ == "__main__":
    json_file1 = 'test1.json'
    json_file2 = 'test2.json'
    compare(json_file1, json_file2)
