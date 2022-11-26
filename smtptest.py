# 此例中从QQ邮箱向outlook邮箱发送邮件
# 要设置QQ邮箱的POP3/SMTP服务开启

import smtplib
import getpass
from email.mime.text import MIMEText
from email.header import Header

sender='.....@qq.com' # QQ邮箱
pwd='.....'  # 打开 POP3/SMTP服务时会获得一个密码
receiver=['.....@outlook.com']
subject='这是一个发送邮件脚本的测试 Python SMTP test' # 邮件主题

msg=MIMEText('这是来自Python smtplib 模块发送的邮件_1','plain','utf-8')
msg['Subject']=subject
msg['From']=sender
msg['To']=','.join(receiver)


try:
	smtpObj=smtplib.SMTP_SSL('smtp.qq.com',587) # QQ邮箱的SMTP服务器及端口，easy to find out, just baidu it
	smtpObj.login(sender,pwd)
	smtpObj.sendmail(sender,receiver,msg.as_string())
	print('Sent successfully')
except smtplib.SMTPException:
	print('Fail to send email')