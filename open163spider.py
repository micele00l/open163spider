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
list_chinese=[]
list_mp4=[]
#构造2个字典
def ddict():
    #将新文件名及id一一对应
    for chinese_name in result_html:
        name_string = chinese_name[73:-4]
        id_string = chinese_name[54:62]
        list_chinese.append(name_string)
    for mp4_name in result_html2:
        list_mp4.append(mp4_name)
def make_mp4file():
    for i in list_mp4:
        f=open('%s' %i,'w')
        f.close()
def change_name():
    for i in os.listdir('.'):
        for k in new_dict:
            if i == k:
                os.rename(i,new_dict[k] + " " + i)
 
ddict()
new_dict = dict(zip(list_mp4, list_chinese))
#make_mp4file()
change_name()
