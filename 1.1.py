# define wariables
City = []
Education = []
Age = []
count = 0
q_final = []
# read from txt file
with open('q.txt') as q_file:
    q_file_read = q_file.readlines()
# cleaning text
q_split = str(q_file_read).split('\\n')
q_split_striped = ""
for i in q_split:
    q_split_striped += i.strip("', ")
# correct lines with mistaces
q_split_striped_split = q_split_striped.split('"')
q_split_striped_split[0:1] = ""
q_split_striped_split[31] = ",high school,31"
q_split_striped_split += ["Kansas City"] + [",graduate degree,21"]
q_split_striped_split[111] = ",college,27"
q_split_striped_split += ["Albuquerque"] + [",graduate degree,28"]
#separate age from degree
for i in range(len(q_split_striped_split)):
    if i%2 == 1:
        q_final += [q_split_striped_split[i].split(',')]
    else:
        q_final += [q_split_striped_split[i]]
# build separate lists "City", "Education", "Age"
for i in range(0,len(q_split_striped_split),2):
    City += [q_split_striped_split[i]]
for j in range(1,len(q_final),2):
    Education += [q_final[j][1]]
for k in range(1,len(q_final),2):
    Age += [q_final[k][2]]
# combine "City", "Education", "Age" in to dict == {City:[Education,age]}
Dict = {}
for i in range(len(City)):
    if City[i] in Dict:
        Dict[City[i]] += [[Education[i], Age[i]]]
    else:
        Dict[City[i]] = [[Education[i],Age[i]]]
    
print(Dict)
city = False
education = False
age = False


                   




