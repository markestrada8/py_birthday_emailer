import datetime as dt
import smtplib
import pandas
import random

sender_email = <origin_email>
password = <app_password>

# 1. Update the birthdays.csv

birthdays_df = pandas.read_csv("birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv

for index, row in birthdays_df.iterrows():
    if dt.datetime(year=row.year, month=row.month, day=row.day).day == dt.datetime.now().day:

        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt", "r") as letter:
            message = letter.read().replace("[NAME]", row["name"])

            # 4. Send the letter generated in step 3 to that person's email address.
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()

                connection.login(user=sender_email, password=password)
                connection.sendmail(
                    from_addr=sender_email,
                    to_addrs=row.email,
                    msg=f"Subject:Happy Birthday!\n\n{message}!"
                )
