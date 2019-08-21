# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 17:07:11 2019

@author: ACER
"""

import math
import re
import os
try: 
  import xml.etree.cElementTree as ET 
except ImportError: 
  import xml.etree.ElementTree as ET 
import sys
  
#xml_filepath = os.path.abspath("./2018test_keywords3.xml")
xml_filepath=os.path.abspath("./2019test_keywords3.xml")
# 得到文件对象

try: 
  tree = ET.parse(xml_filepath)     #打开xml文档 
  root = tree.getroot()         #获得root节点  
except Exception: 
    print ("Error:cannot parse file xml.")
    sys.exit(1) 
   
j = 0
content = ""
for top in root.findall('top'): #找到root节点下的所有top节点 

    text = "#weight("

    num = top.find('num').text   #子节点下节点num的值 
    body = top.find('body').text  #子节点下节点body的值 
    whole_words = top.find('whole_keywords').text
    num = re.sub("\D", "", num)
    
    content += "<query><number>" + num + "</number>"

    whole_text = body.splitlines()
    whole_keywords = whole_words.splitlines()
    for keywords in whole_keywords:
        text += "0.2 #1(" + keywords + ") "
    #print(text)
    length = len(whole_text)
    five_part = math.ceil(length/5)
    #print(five_part)
    #print(length)
    
    text1 = text  #存储前1/5的段落内容
    text2 = text  #存储中间3/5的段落内容
    text3 = text  #存储后1/5的段落内容
    
    for words in top.findall('para_keywords'):
        #print(type(words.text))
        #print(type(words.attrib['number']))
        part_keywords = str(words.text).splitlines()

        for keywords in part_keywords:
            if int(words.attrib['number']) < five_part+1:
                text1 += "0.8 #1(" + keywords + ") "
            elif five_part < int(words.attrib['number']) < length-five_part+1:
                text2 += "0.8 #1(" + keywords + ") "
            elif int(words.attrib['number']) > length-five_part:
                text3 += "0.8 #1(" + keywords + ") "
    #print(text1)
    #print(text2)
    #print(text3)
    content += "<text>" + text1 + ")</text></query>"
    content += "<query><number>" + num + "</number>" + "<text>" + text2 + ")</text></query>"
    content += "<query><number>" + num + "</number>" + "<text>" + text3 + ")</text></query>"
    
    #print(content+"/n")
    
with open("D:\\temp1.txt", "w", encoding='utf-8') as f:
    f.write(content)
    f.close()
        
    
     
    
    
