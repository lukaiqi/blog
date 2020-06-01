import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


class Mail(object):
    def __init__(self):
        # 邮件相关
        self.my_sender = '17313134897'  # 发件人邮箱账号
        self.my_pass = 'Lukaiqi189.cn'  # 发件人邮箱密码

    def send(self, address, message):
        msg = MIMEText(str(message))
        msg['From'] = formataddr(["梦落无声", self.my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["", address])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "用户注册验证码邮件"  # 邮件的主题

        server = smtplib.SMTP_SSL("smtp.189.cn", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(self.my_sender, self.my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(self.my_sender, [address, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
