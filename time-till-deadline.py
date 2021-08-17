import datetime

date_time = input("enter your goal with a deadline separated by colon\n")
input_list = date_time.split(":")

goal = input_list[0]
deadline = input_list[1]

date_deadline = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today = datetime.datetime.today()

time_till = date_deadline - today

print(f"Dear user! Time remaining to your goal : {goal} is {time_till.days} days")










