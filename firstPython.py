# -*- coding: utf-8 -*-
import base64
import json
import qrcode


def base64_encode():
    string_to_be_processed = input("输入要加密的字符串:\n")
    string_after_processed = base64.b64encode(string_to_be_processed.encode('utf-8'))
    string_after_processed_twice = str(string_after_processed)[2:-1]
    print(string_after_processed_twice)


def base64_decode():
    string_to_be_processed = input("输入要解密的字符串:\n")
    try:
        string_after_processed = str(base64.b64decode(string_to_be_processed), "utf-8")
        string_after_processed = str(string_after_processed)

        print(string_after_processed)
    except Exception as e:
        print("解密出错，错误信息：")
        print(e)


def json_and_dic():

    dic = {}
    x_result = 0
    while x_result == 0:
        x = input("请输入键值对数目：")
        try:
            x = int(x)
            x_result = 1
        except Exception as e:
            print("请输入数字")

    for i in range(0, x):
        key = ""
        key_result = 0
        value = ""
        value_result = 0
        while key == "" or key in dic.keys():
            if key in dic.keys():
                print("键已存在")
                key = input("请输入键：")
            else:
                key = input("请输入键：")
        while value == "":
            value = input("请输入值：")
        dic[key] = value

    dic_after = {}
    for key in dic.keys():
        new_value = key
        new_key = dic[key]
        if new_key in dic_after.keys():
            new_list = []
            for value_2_key in dic.keys():
                if dic[value_2_key] == new_key:
                    new_list.append(value_2_key)
            new_value = str(new_list)
            new_value_list = new_value
            new_value = new_value_list
        dic_after[new_key] = new_value

    print("反转后的字典：" + str(dic_after))
    print(type(dic_after))
    # json.dumps()方法可以将字典转换成json字符串
    ss_json = json.dumps(dic)
    print("json字符串：" + ss_json)
    print(type(ss_json))


def create_qrode():
    file = open(r'C:\Users\86180\Desktop\自强考核.txt', encoding='utf-8')
    text = file.read()
    print(text)
    img = qrcode.make(text)
    img.save("result.jpg")
    print("二维码以保存")


while True:
    print("1. base64加密")
    print("2. base64揭秘")
    print("3. json和字典")
    print("4. 退出")
    status = input("请输入操作：")
    if status == '1':
        base64_encode()
    elif status == '2':
        base64_decode()
    elif status == '3':
        json_and_dic()
    elif status == '4':
        break
    else:
        print("请重新输入")
