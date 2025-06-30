import datetime as dt
import random
import pandas as pd
import smtplib

MY_EMAIL = "youremail@gmail.com"
MY_PASSWORD = "yourpassword"

now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    num = random.randint(1,3)
    with open(f"letter_templates/letter_{num}.txt") as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person["email"], msg=f"Subject: Happy birthday!\n\n {contents}")
