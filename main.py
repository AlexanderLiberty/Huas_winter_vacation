#!/usr/bin/env python
#  -*- coding:utf-8 -*-
#2022.01.28 
#2022.01.28,破解加密算法，文本中可以直接填写明文
#打卡日期跟随系统日期，无需手动修改
#by Alexander Liberty

import json
import requests
from http import cookiejar
import time

#没有票据，注意两个值的变量，//Referer、Cookie
headers = {'Host': 'www.huas.edu.cn:319',
'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36',
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'X-Requested-With': 'XMLHttpRequest',
'Content-Length': '58',
'Origin': 'http://www.huas.edu.cn:319',
'Connection': 'close'}

#获取MD5加密密码
def md5sign(passwd):
	rqpasswd = {'p':'mypswd'}
	rqpasswd['p'] = passwd
	rqmd5 = requests.get("https://tools.pswd.icu/password/pswd.php",params=rqpasswd)
	return rqmd5

#拿取票据
def sign():
	#密码直接填写明文即可
	fromdata = {'uname':'填学号','pd_mm':'填明文密码'}
	pd_mm = fromdata['pd_mm']
	pd_mm = md5sign(pd_mm)
	fromdata['pd_mm'] = pd_mm.text
	rqs = requests.post("http://www.huas.edu.cn:319/website/login",headers=headers,data=fromdata)
	cookie = requests.utils.dict_from_cookiejar(rqs.cookies)
	return cookie


#打卡内容，dkdz,API定位地点，dkd,打卡地点，dkly,打卡地点来源，dkd,自己填写的地址，jzdValue,区号，，jzdSheng.dm,省代码，jzdShi.dm市代码，jzdXian.dm,县代码，jzdDz,家庭地址，jzdDz2,家庭地址2，lxdh,手机号，sfzx1,在校状态，fbrq,fxrq打卡日期，operationType,操作类型
data = {'dkdz':'API定位地点','dkly':'baidu','dkd':'湖南省长沙市','jzdValue':'省级代码%2C市级代码%2C县级代码','jzdSheng.dm':'省级代码','jzdShi.dm':'市级代码','jzdXian.dm':'县级代码','jzdDz':'这里填家庭地址','jzdDz2':'这里填家庭地址','lxdh':'填写手机号','sfzx':'0','sfzx1':'%E4%B8%8D%E5%9C%A8%E6%A0%A1','twM.dm':'01','tw1':'%5B35.0~37.2%5D%E6%AD%A3%E5%B8%B8','yczk.dm':'01','yczk1':'%E6%97%A0%E7%97%87%E7%8A%B6','fbrq':'todaytimes','jzInd':'0','jzYy':'','zdjg':'','fxrq':'todaytimes','brStzk.dm':'01','brStzk1':'%E8%BA%AB%E4%BD%93%E5%81%A5%E5%BA%B7%E3%80%81%E6%97%A0%E5%BC%82%E5%B8%B8','brJccry.dm':'01','brJccry1':'%E6%9C%AA%E6%8E%A5%E8%A7%A6%E4%BC%A0%E6%9F%93%E6%BA%90','jrStzk.dm':'01','jrStzk1':'%E8%BA%AB%E4%BD%93%E5%81%A5%E5%BA%B7%E3%80%81%E6%97%A0%E5%BC%82%E5%B8%B8','jrJccry.dm':'01','jrJccry1':'%E6%9C%AA%E6%8E%A5%E8%A7%A6%E4%BC%A0%E6%9F%93%E6%BA%90','jkm':'','jkm1':'','xcm':'','xcm1':'','xgym':'','xgym1':'','hsjc':'','hsjc1':'','bz':'这里填写备注，如果没有则删除','operationType':'Create','dm':''}


if __name__ == "__main__":
	#先拿票据
	cookies = {}#初始化cookie
	cookies = sign()
	
	#获取今天的日期
	today = time.strftime("%Y-%m-%d", time.localtime())
	todays = print(today)
	for k in data:
		if data[k] == "todaytimes":
			data[k] = today
	
	#拿到票据后进行打卡
	requests.post("http://www.huas.edu.cn:319/content/student/temp/zzdk?_t_s_=1643436248496",headers=headers,cookies=cookies,data=data)
	
	print(res.text)
