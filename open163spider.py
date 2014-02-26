#coding:utf-8
import re
import urllib2
import os

url = "http://v.163.com/special/opencourse/buildingdynamicwebsites.html"
html_source = urllib2.urlopen(url).read()
#re_html = re.compile(r'<a\s*href="http://v.163.com/movie[^>]*(.*?)a>')
re_html = re.compile(r'<a\s*href="http://v.163.com/movie[^>]*>[^<]+</a>')
result_html = re_html.findall(html_source)
re_html2 = re.compile(r'[^\s]{9}\.mp4') 
result_html2 = re_html2.findall(html_source)
name_dict = {}
name_dict2 = {}
new_dict={}
#构造2个字典
def ddict():
    #将新文件名及id一一对应
    for item in result_html:
        name_string = item[73:-4]
        id_string = item[54:62]
        name_dict[id_string] = name_string
        for item2 in result_html2:
            name_dict2[item2] = id_string
            new_dict[name_string] = item2 
 
#def change_file_name():

ddict()
#change_file_name()
print name_dict
value_list =  name_dict2.values()
print value_list
print new_dict.keys()
#change_file_name()
