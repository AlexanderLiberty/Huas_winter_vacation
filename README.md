# Huas_winter_vacation
使用请遵守相关法律法规和防疫要求，我一直呆在家不出门所以要把这种繁琐的工作交给计算机去完成。注意：  
<h3 style="color:Tomato;">请自觉遵守防疫要求！！！</h3>

# 使用前注意
## 用户标识
- 15行'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36',
### 将里面的字段替换成相应的手机型号，如：
* 手机型号Iphone替换为:  
`'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',`
- Firefox for iOS:  
`'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) FxiOS/7.5b3349 Mobile/14F89 Safari/603.2.4',`
- Android:  
`'User-Agent': 'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',`
- Firefox for Android:  
`'User-Agent': 'Mozilla/5.0 (Android 7.0; Mobile; rv:54.0) Gecko/54.0 Firefox/54.0',`
- Chrome手机:  
`'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36',`
* Opera Mobile (Blink rendering engine):  
`'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-A310F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/42.7.2246.114996',`

## 将修改字段内容
- 35行填写学号和密码
- 45行填写下面的信息

## key
**dkdz**，API定位地点,通过IP路由进行地址确认，不精准随便填一个家附近的地址就可以了(要改，url编码)  
**dkd**,打卡地点，精确到市名(要改，url编码)  
dkly,打卡地点来源(默认不要改)  
**jzdValue**,区号(省代码%2c市代码%2c县代码)这里的代码就是户籍代码，如：湖南省娄底市,'jzdValue':'430000%2C431300%2C431301'  
**jzdSheng.dm**,省代码(要改)，如：'jzdShi.dm':'430000'  
**jzdShi.dm**,市代码(要改)，如：'jzdShi.dm':'431300'  
**zdXian.dm**,县代码(要改)，如：'zdXian.dm':'431301'  
**jzdDz**,家庭地址(要填，中文)  
**jzdDz2**,家庭地址2(要填，中文)  
**lxdh**,手机号(要填)  
**sfzx1**,在校状态(不在校默认就可以)  
fbrq,fxrq打卡日期(不用改)  
**bz**,备注(没有额外备注删除中文，为空即可)，为空如：'bz':''  
operationType,操作类型(不用管)  

将字段中的汉字进行url编码再填如键值对中，其中"dkdz"、"jzdDz"、"jzdDz2"和"bz"一定要使用中文，否则无法正常显示  
:)

## 云函数部署
### 1.创建云函数
![Serverless1](/images/Serverless1.jpg?raw=true "Serverless1")
### 2.将修改后的代码复制进去
![Serverless2](/images/Serverless2.jpg?raw=true "Serverless2")
### 3.将执行超时时间改大
![Serverless3](/images/Serverless3.jpg?raw=true "Serverless3")
### 4.设置定时触发时间，具体查看云函数配置文档
![Serverless4](/images/Serverless4.jpg?raw=true "Serverless4")
### 5.本地调试，打卡成功后会返回，云打卡返回可能不正常，但是会打卡成功
{"errorInfoList":[],"result":true,"msg":null}  
![Good](/images/Good.jpg?raw=true "Good")

# MIT License

Copyright (c) 2022 Александр Свобода

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
