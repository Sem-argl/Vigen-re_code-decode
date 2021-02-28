import random

num_people_in_room = 40
birthday_mach_list = {}
birthday_list1 = {}
month = ""

#===  Simulate situation
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for i in range(1,num_people_in_room + 1):
  month = random.choice(months)
  if month == "February":
     day = random.randint(1,28)
  elif months == "January" or "March" or "May" or "July" or "August" or "October" or "December":
    day = random.randint(1,31)
  else:
    day = random.randint(1,30)
  if month in birthday_list1:
    birthday_list1[month] += [day]
  else:
    birthday_list1[month] = [day]     # dictionary ith simulated birth days

# === count number of people with same birth date

for birth_month in birthday_list1:
    for day in birthday_list1[birth_month]:
      if birthday_list1[birth_month].count(day) > 1:
          birthday_mach_list[birth_month] = [day,birthday_list1[birth_month].count(day)]
    
#print(birthday_mach_list)
t = 0
for i in birthday_mach_list:
  t += birthday_mach_list[i][1]
print("In our simulation, there is ", t,   " people have the same birthdays. \non this dates:",birthday_mach_list)
