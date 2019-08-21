# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 16:21:09 2019

@author: ACER
"""

import os
import re
import xml.etree.ElementTree as ET
import sys

root = os.getcwd()  # 获得当前路径 /home/dir1
whole_content = ""
try:
    file = open(root + '\\entity2019.txt', 'r', encoding='utf-8')  # 以读模式打开文件
except FileNotFoundError:  # 如果文件不存在，给提示
    print("file is not found")
else:
    line = file.readline()  # 读取第一行
    while line:
        tup1 = line.partition(' ')[2].partition(' ')[0]
        tup2 = line.partition(' ')[2].partition(' ')[2]
        length = tup1.partition("=")[2]
        mth=re.findall("'.+?'",tup2)

        i = 0
        content = ""
        max = int((int(length))/100)
        for m in mth:
            i = i + 1
            if i < max:
                content = content + m.replace("'","") + "\n"
            elif i == max:
                content = content + m.replace("'","")
        #print(content)
        whole_content += content + "?"
        line = file.readline()  # 继续读取下一行
        
xmlFilePath = os.path.abspath(root + '\\2019test_keywords1.xml')
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
    node1 = ET.Element("whole_entities")
    node1.text = whole_content.split("?")[i]
    child.append(node1)
    i += 1

tree.write('D://2019test_keywords2.xml', encoding='utf-8', xml_declaration=True)
