import datetime as dt
import os
import random
import smtplib
import pandas

my_email = os.environ["EMAIL"]
password = os.environ["PASS"]

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

# list comp
# (new_item for item in list)

# dict comp
# {(new_key, new_value) : row for (key, value) in dict}

# dict comp dataframe
# {(new_key, new_value) : data_row for (key, value) in data.iterrows()}

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]

    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}")
