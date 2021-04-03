import requests
import base64
import hashlib

image_dict = {

}



def get_base64_data(page_num):
    url = f"http://match.yuanrenxue.com/api/match/4?page={page_num}"
    headers = {}
    res = requests.get(url=url, headers=headers)
    return res.json()['info'], res.json()['key'], res.json()['value']


# 利用key,value计算出属性为display = none的md5 索引值
def get_j_key(key, value):
    str_date = (key + value).encode("ascii")
    str_date = base64.b64encode(str_date).decode("utf-8").replace("=","")
    md5 = hashlib.md5()
    md5.update(str_date.encode("utf-8"))
    return md5.hexdigest()

def caculate_css_left(number_style_list,num_list):
    number_style_list = [int(__) / 11 for __ in number_style_list]
    ture_order_list = [None] * len(number_style_list)
    for index, number_style in enumerate(number_style_list):
        ture_order_list[int(index + num_list)] = num_list[index]
    return ture_order_list
if __name__ == '__main__':
    black,key,value = get_base64_data(1)
    md5_value = get_j_key(key,value)
    print(black)
    print(md5_value)


