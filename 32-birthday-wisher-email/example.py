# import smtplib

# my_email = "paulinehuby.collegemaisonneuve@gmail.com"
# # Generated App Password from gmail
# app_password = "zyezxksyevfvlkyj"

# # Defines an SMTP client session
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     # Secures the connexion by encrypting infos
#     connection.starttls()
#     # Log in
#     connection.login(user=my_email, password=app_password)
#     # Send email
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="huby.pauline@gmail.com",
#                         msg="Subject:Hello\n\nThis is the body of my email.")


# DATETIME -------------------------------------------------------

import datetime as dt
import random

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
date_of_birth = dt.datetime(year=1995, month=12, day=15)

print(now)

with open("32-birthday-wisher-email/quotes.txt") as file:
    quote_list = [quote for quote in file]
    random_quote = random.choice(quote_list)
    print(random_quote)
