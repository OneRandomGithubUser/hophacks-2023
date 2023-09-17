# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
import csv

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
def send_text(phone_number,name, pills):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body=f"Reminder {name}! Take your {pills} pills",
                         from_='++18883401803',
                         to='+' + phone_number
                     )

    print(message.sid)


if __name__ == "__main__":
    with open('/Users/dylanconnolly/PycharmProjects/Competitive_Coding/database.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            pills = []
            j = 0
            for i in row[9:]:
                j += 1
                if j%3==0:
                    pills.append(i)
            if len(pills) == 0:
                continue
            if len(pills) == 1:
                pillname = pills[0]
            elif len(pills) == 2:
                pillname = pills[0] + " and " + pills[1]
            elif len(pills) >= 3:
                pills[-1] = 'and ' + pills[-1]
                pillname = ", ".join(pills)
            print(pillname)
            number = row[2]
            name = row[0]
            print(pillname)
            # send_text(number, name, pillname)
