oimport yake
import xml.dom.minidom as xmldom
import os

xml_filepath = os.path.abspath("./2018test_full.xml")
# xml_filepath=os.path.abspath("./2019test_full.xml")
# 得到文件对象
dom_obj = xmldom.parse(xml_filepath)

# 得到元素对象
element_obj = dom_obj.documentElement

# 获得子标签

sub_element_obj = element_obj.getElementsByTagName("top")

for i in range(len(sub_element_obj)):
    sub_element_obj1 = sub_element_obj[i].getElementsByTagName("num")
    sub_element_obj2 = sub_element_obj[i].getElementsByTagName("body")
    print(sub_element_obj1.firstChild.data, end='\t')
    print(sub_element_obj2.firstChild.data, end='\t')
    print()

    text = sub_element_obj2.firstChild.data

    # assuming default parameters
    simple_kwextractor = yake.KeywordExtractor()
    keywords = simple_kwextractor.extract_keywords(text)

    for kw in keywords:
        print(kw)

    # specifying parameters
    max_ngram_size = 3
    custom_kwextractor = yake.KeywordExtractor(lan="en", n=max_ngram_size, dedupLim=0.9, dedupFunc='seqm',
                                               windowsSize=1, top=20, features=None)

    keywords = custom_kwextractor.extract_keywords(text)

    for kw in keywords:
        print(kw)


