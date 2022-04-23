import smtplib
import datetime as dt
import random

now = dt.datetime.now()
with open("quotes.txt","r") as quotes:
    lines = quotes.readlines()
    quote_to_send = random.choice(lines)
    if dt.date.today().weekday() == 0:

        my_mail = "ashwinpremnath4010@gmail.com"
        password = "amuthachandran"

        connection = smtplib.SMTP("smtp.gmail.com",587)
        connection.starttls()
        connection.login(user=my_mail,password=password)
        connection.sendmail(from_addr=my_mail, to_addrs="ashwinpremnath123@gmail.com",msg=f"{quote_to_send}")
        connection.close()
