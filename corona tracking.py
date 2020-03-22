import codecs
import random
from datetime import datetime


def unique(list1):
    # intilize a null list
    unique_list = []

    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
            # print list
    for x in unique_list:
        print (x)

    #list of places
with codecs.open('D:/Acellere/corona virus/list of places in germany.txt', 'r', 'utf-8') as f:
    #lines = f.readlines('\n')
    list_of_places = f.read().splitlines()
print(list_of_places)

# 100 people visitng a place a day
patients_visit = []
for i in range (1, 101):
    one_patient_visit = []
    for j in range(1, 15):
        one_patient_visit.append(random.randrange(1, 65, 1))
    patients_visit.append(one_patient_visit)
print(patients_visit)
# dates of ifection of 100 patients
with codecs.open('D:/Acellere/corona virus/date of infection for 100 patients.txt', 'r', 'utf-8') as f:
    #lines = f.readlines('\n')
    date_of_infection = f.read().splitlines()
#print(date_of_infection)

#TBD
# take input as 1st date and find who got infection on that date
#sample input date is 12-03-2020

date_string = "12-03-2020"

places_visited = []

for i in range (1, 100):
    #if date_of_infection[i]==datetime.strptime(date_string, format):
    #print("patient done: ", i+1)
    if date_of_infection[i] == date_string:
        print("patient {%d} got infected on {%s}", i+1, date_string)
        places_visited.append(patients_visit[i][0])
        print("patient visited this place", i, patients_visit[i][0])

print(places_visited, len(places_visited))

previously_infected_patients = []

for i in range (0, 100):
    input_date = datetime.strptime(date_string, '%d-%m-%Y')
    p_date = datetime.strptime(date_of_infection[i], '%d-%m-%Y')
    #print("difference between infection date and something is ", (input_date-p_date).days)
    if (input_date-p_date).days<0:
        for j in range (2, 14):
            for k in range (0, len(places_visited)-1):
                temp = places_visited[k]
                if patients_visit[i][j] == places_visited[k]:
                    print("previous patient = ", i)
                    previously_infected_patients.append(i)

print("All the patients that were at the same place as the patients who got corona on", date_string)
unique(previously_infected_patients)

print("Places at which they got corona")
for i in range (0, len(places_visited)):
    print(list_of_places[places_visited[i]])

