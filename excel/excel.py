import pandas as pd

clientfee = pd.read_csv('clientfee--230320.csv')
hulderjour = pd.read_csv('holderjour--230320.csv')

c_list = clientfee.values.tolist();
h_list = hulderjour.values.tolist();
print('clientfee--230320.csv 有 {} 行'.format(len(c_list)), )
print('holderjour--230320.csv 有 {} 行'.format(len(h_list)))

c_dict = {}
for i in c_list:
    client_id = str(i[0]).replace(" ","")
    key_info = str(i[1]).replace(" ","")
    key = client_id + ';' + key_info;
    if c_dict.get(key) is not None:
        raise Exception(key, '重复')
    c_dict.update({key : ''})

h_dict = {}
for i in h_list:
    client_id = str(i[1]).replace(" ","")
    key_info = str(i[2]).replace(" ","") + ";" + \
        str(i[3]).replace(" ","") + ";" + \
        str(i[4]).replace(" ","") + str(i[5]).replace(" ","") + ";" + \
        str(i[6]).replace(" ","") + ";"
    key = client_id + ';' + key_info;
    if h_dict.get(key) is not None:
        raise Exception(key, '重复')
    h_dict.update({key : ''})

print("----------------------------------------------")

match_count = 0
diff_count = 0
for key in h_dict:
    if key not in c_dict.keys():
        diff_count += 1
        print('缺少', key)
    else:
        match_count += 1
print('存在差异的数量', diff_count)
print('匹配相同的数量', match_count)

print("----------------------------------------------")