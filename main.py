import smtplib
import datetime as dt
import random

now=dt.datetime.now()
day=now.weekday()
if(day==6):
    with open("quotes.txt","r") as quotesfile:
        allquotes=quotesfile.readlines()
        qu=random.choice(allquotes)
    myemail="sayantikahacky@gmail.com"
    passworde="abcd1234()"
    connection=smtplib.SMTP("smtp.gmail.com",port=587)
    connection.starttls()
    connection.login(user=myemail,password=passworde)
    connection.sendmail(from_addr=myemail,
    to_addrs="harshitkeshari30@gmail.com",
    msg=f"Subject:Testing automated email\n\n{qu}")
    connection.close()

