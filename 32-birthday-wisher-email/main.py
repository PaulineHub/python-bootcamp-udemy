from datetime import datetime 
import pandas

today_tuple = (datetime.now().month, datetime.now().day)
data = pandas.read_csv("32-birthday-wisher-email/birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv
# birthdays_dict = {
#     (month, day): data_row
# }
# pandas.DataFrame.iterrows : Iterate over DataFrame rows as (index, Series) pairs.
birthdays_dict = {
    (data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()
}

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents.replace("[NAME]", birthday_person["name"])



# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



