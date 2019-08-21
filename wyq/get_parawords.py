# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 16:23:08 2019

@author: ACER
"""

import yake
import os
try: 
  import xml.etree.cElementTree as ET 
except ImportError: 
  import xml.etree.ElementTree as ET 
import sys
  
#xml_filepath = os.path.abspath("./2018test_keywords2.xml")
xml_filepath=os.path.abspath("./2019test_keywords2.xml")
# 得到文件对象

try: 
  tree = ET.parse(xml_filepath)     #打开xml文档 
  root = tree.getroot()         #获得root节点  
except Exception: 
    print ("Error:cannot parse file xml.")
    sys.exit(1) 
   
j = 0
for top in root.findall('top'): #找到root节点下的所有top节点 
    num = top.find('num').text   #子节点下节点num的值 
    body = top.find('body').text  #子节点下节点body的值 

    whole_text = body.splitlines()
    j += 1
    #print(whole_text)
    
    k = 0
    for text in whole_text:
        if text.strip():
            # assuming default parameters
            i = 0
            content = ""
            simple_kwextractor = yake.KeywordExtractor()
            keywords = simple_kwextractor.extract_keywords(text)

            for kw in keywords:
                if i < 1:
                    content += kw[0] + "\n"
                elif i == 1:
                    content += kw[0]
                i += 1
            
            print(content)
            k += 1
    
            node1 = ET.Element("para_keywords",{"number":str(k)})
            node1.text = content
            top.append(node1)

    
tree.write('D://2019test_keywords3.xml', encoding='utf-8', xml_declaration=True)
 