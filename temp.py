import re
import os

from selenium import webdriver
pattern = re.compile(r'^[0-9a-zA-Z_]+$')
str = 'a。'
print(type(pattern.search(str)))

str1 = '47530954_aaa'
print(pattern.search(str1),type(pattern.search(str1)))


x="《》"

print(re.search(r"^[^`~!@#%^&*()_+=|{}':;""<>'/?,]*$",x))

print(os.getcwd())
f=open(r"/setests/keyMouse/20201028.py",mode='r')

f.close()


import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 第三方 SMTP 服务
#mail_host = "smtp.qq.com"  # 设置服务器
#mail_user = "530735660@qq.com"  # 用户名
#mail_pass = "yqdzzbjfxhidbhea"  # 口令

sender ='530735660@qq.com'
receivers = ['530735660@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 创建一个带附件的实例
message = MIMEMultipart('related')
message['From'] = Header("杨小景发", 'utf-8')
message['To'] = Header("杨小景收", 'utf-8')
subject = '自动化测试报告'
message['Subject'] = Header(subject, 'utf-8')

# 邮件正文内容
# message.attach(MIMEText('这是自动化测试报告……', 'plain', 'utf-8'))


#邮件带html和链接
msgAlternative = MIMEMultipart('alternative')
message.attach(msgAlternative)

mail_msg = """
<p>Python 自动化测试邮件...</p>
<p><a href="http://www.runoob.com">菜鸟教程链接</a></p>
<p>图片演示：</p>
<p><img src="cid:image1"></p>
"""
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

# 指定图片为当前目录
fp = open('test.jpg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<image1>')
message.attach(msgImage)


# 构造附件1，传送相应目录下的 报告文件文件
#C:\Windows\System32\config\systemprofile\AppData\Local\Jenkins\.jenkins\workspace\testgithub\test_reports\TEST-AutoTest-20201122191115.xml
att1 = MIMEText(open(r'C:\Windows\System32\config\systemprofile\AppData\Local\Jenkins\.jenkins\workspace\testgithub\test_reports\TEST-AutoTest-20201122191115.xml', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="TEST-AutoTest-20201122191115.xml"'
message.attach(att1)

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect('smtp.qq.com', '25')
    smtpObj.login('530735660@qq.com', 'vzxybkazlsxbcbcg')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")

