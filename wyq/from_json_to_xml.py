# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 10:32:48 2019

@author: JadeW
"""
import os
import json
import re
import xml.etree.ElementTree as ET
import sys

#遍历xml文件
def traverseXml(element):
    #print (len(element))
    if len(element)>0:
        for child in element:
            print (child.tag, "----", child.attrib)
            traverseXml(child)
    #else:
        #print (element.tag, "----", element.attrib)

def get_value():
    root = os.getcwd()  # 获得当前路径 /home/dir1
    title_value = []
    body_value = []
    try:
        file = open(root + '\\2018test_json.txt', 'r', encoding='utf-8')  # 以读模式打开文件
    except FileNotFoundError:  # 如果文件不存在，给提示
        print("file is not found")
    else:
        line = file.readline()  # 读取第一行
        while line:
            i = 0
            line_json = json.loads(line)  # 转化为json格式
            temp_body = ''
            title_value.append(line_json['title'])
            #print(line_json['title'])
            while i < len(line_json['contents']):
                if "subtype" in line_json['contents'][i]:
                    if line_json['contents'][i]["subtype"] == 'paragraph':
                        temp_body += re.sub('\\<.*?\\>', '', line_json['contents'][i]['content'])
                        #print(re.sub('\\<.*?\\>', '', line_json['contents'][i]['content']))
                        temp_body += "\n"
                    elif line_json['contents'][i]["subtype"] == 'blockquote':
                        temp_body += re.sub('\\<.*?\\>', '', line_json['contents'][i]['content'])
                        #print(re.sub('\\<.*?\\>', '', line_json['contents'][i]['content']))
                        temp_body += "\n"
                    i = i + 1
                else:
                    i = i + 1
            body_value.append(temp_body)
            line = file.readline()  # 继续读取下一行
    return title_value,body_value

if __name__ == "__main__":
    root = os.getcwd()  # 获得当前路径 /home/dir1
    (title_value,body_value) = get_value()
    print(title_value)
    print(body_value)
    xmlFilePath = os.path.abspath(root + '\\2018test_original.xml')
    try:
        tree = ET.parse(xmlFilePath)
        # 获得根节点
        root = tree.getroot()
    except Exception as e:  # 捕获除与程序退出sys.exit()相关之外的所有异常
        print("parse test.xml fail!")
        sys.exit()

    i = 0
    # 遍历root的下一层
    for child in root:
        node1 = ET.Element("title")
        node1.text = title_value[i]
        node2 = ET.Element("body")
        node2.text = body_value[i]
        child.append(node1)
        child.append(node2)
        i += 1

    tree.write('D://2018test_full.xml', encoding='utf-8', xml_declaration=True)