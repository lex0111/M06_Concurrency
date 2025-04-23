#Lexus Aguilera
#M06 Programming Assignment

#13.1
import datetime

today = datetime.date.today()
with open('today.txt', 'w') as file:
    file.write(today.isoformat())

#13.2
with open('today.txt', 'r') as file:
    today_string = file.read()

#13.3
parsed_date = datetime.datetime.strptime(today_string, '%Y-%m-%d').date()
print(parsed_date)
