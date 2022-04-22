import smtplib

my_mail = "ashwinpremnath4010@gmail.com"
password = "amuthachandran"

connection = smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login(user=my_mail,password=password)
connection.sendmail(from_addr=my_mail, to_addrs="ashwinpremnath123@gmail.com",msg="Hello")
connection.close()