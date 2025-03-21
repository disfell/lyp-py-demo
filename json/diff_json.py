import json

from deepdiff import DeepDiff


def compare(json1, json2, path=None):
    """
    比较两个json文件是否一致
    :param json1: 文件的绝对路径(需要比对的第一个json文件)
    :param json2: 文件的绝对路径(需要比对的第二个json文件)
    :param path: 需要比对的 json 节点比如 user.name，输入 None 则是比对整个 json
    :return:
    """
    with open(json1) as json1, open(json2) as json2:
        d1 = json.load(json1)
        d2 = json.load(json2)
        node1 = d1
        node2 = d2
        if path is not None:
            for key in path.split('.'):
                node1 = node1[key]
                node2 = node2[key]
        diff = DeepDiff(node1, node2, ignore_order=True, view='tree')
        print(diff.pretty())


if __name__ == '__main__':
    compare('/Users/lyp/Downloads/tmps/hs.json', '/Users/lyp/Downloads/tmps/hs_ufics.json', None)
