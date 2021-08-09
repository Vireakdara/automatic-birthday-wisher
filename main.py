import datetime as dt
import smtplib
import pandas as pd
import random

MY_EMAIL = "nikolalatesting@gmail.com"
MY_PASSWORD = "qwer/.,m1234"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv("birthdays.csv")
birthday_dict = {
    (data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()
}
print(birthday_dict)

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    print(birthday_person)
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_files:
        contents = letter_files.read()
        contents = contents.replace("[NAME]", birthday_person['name'])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person['email'],
                            msg=f"Subject:Happy Birthday!\n\n{contents}")

