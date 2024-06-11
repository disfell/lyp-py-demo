str = 'full_name,client_id,zipcode,organ_flag,is_open_acct,address,organ_prodmana_id_address,organ_pcid_begindate,organ_pcid_enddate,branch_no,nationality,id_begindate,id_enddate,market_code,market_prop,state_owned_prop,register_fund_prop,company_kind,industry_type,work_range,register_fund,register_money_type,city_no,id_address,instrepr_name,instrepr_id_kind,instrepr_id_no,instrepr_id_begindate,instrepr_id_enddate,instrepr_tel,control_holder,control_id_kind,control_id_no,control_id_begindate,control_id_enddate,issued_depart,organ_prodmana_name,organ_prodmana_id_kind,organ_prodmana_id_no,organ_prodmana_begindate,organ_prodmana_enddate,fax,e_mail,prof_organ_flag,three_certificates_flag,organ_prodmana_control_name,organ_prodmana_control_id_kind,organ_prodmana_control_id_no,join_position_str,pos_str,operator_no,op_station,op_entrust_way,office_tel,business_licence,business_licence_begindate,business_licence_enddate,organ_code,organ_code_begindate,organ_code_enddate,tax_register,tax_registe_begindate,tax_registe_enddate,client_id,branch_no,zipcode,address,full_name,organ_flag,id_kind,id_no,nationality,id_begindate,id_enddate,market_code,market_prop,state_owned_prop,register_fund_prop,company_kind,industry_type,work_range,register_fund,register_money_type,city_no,id_address,instrepr_name,instrepr_id_kind,instrepr_id_no,instrepr_id_begindate,instrepr_id_enddate,instrepr_tel,control_holder,control_id_kind,control_id_no,control_id_begindate,control_id_enddate,issued_depart,fax,e_mail,join_position_str,position_str,pos_str,operator_no,op_station,op_entrust_way,office_tel,business_licence,business_licence_begindate,business_licence_enddate,organ_code,organ_code_begindate,organ_code_enddate,tax_register,tax_registe_begindate,tax_registe_enddate,client_id,branch_no,full_name,organ_flag,id_kind,id_no,isexist_controlholder,prof_organ_flag,three_certificates_flag,control_id_kind,control_id_no,organ_prodmana_control_name,organ_prodmana_control_id_kind,organ_prodmana_control_id_no,organ_pcid_begindate,organ_pcid_enddate,organ_prodmana_id_address,join_position_str,position_str,pos_str,operator_no,op_station,op_entrust_way,client_id,branch_no,full_name,organ_flag,organ_prodmana_name,organ_prodmana_id_kind,organ_prodmana_id_no,organ_prodmana_begindate,organ_prodmana_enddate,join_position_str,pos_str,operator_no,op_station,op_entrust_way,organ_prod_info_jour_remark'
items = str.split(",")

# 使用集合来记录已经出现过的元素
seen = set()

# 使用列表推导式来保持顺序并去除重复元素
unique_items = [item for item in items if not (item in seen or seen.add(item))]

# 定义每行显示的元素数量，例如每行显示3个元素
elements_per_row = 1

# 打开一个文件用于写入，如果文件不存在则创建
with open('output.txt', 'w', encoding='utf-8') as file:
    # 遍历列表并写入文件，同时控制换行
    for index, item in enumerate(unique_items):
        # 写入元素，使用逗号和空格作为分隔
        file.write(item + ", ")
        
        # 检查是否到达了行的末尾，如果是，则写入换行符
        if (index + 1) % elements_per_row == 0:  
            file.write("\n")  # 换行