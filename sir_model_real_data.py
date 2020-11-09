import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#****************************************
#************START OF USER BLOCK*********
b = 0.8 # how fast infected
k = 0.33 # how fast recovered
recovered = 0. # number or recovered
infected = 0.00000127 # number of infected
sus = 1. # number of susceptible
t = 0.1 # delta T
N = 1000 # Time steps
death = 0 # initial deaths
days_to_recover = 7 # days to recover
death_rate = 0.01 # initial death rate
overload_death_rate = 0.75 # overlimit death rate
infected_limit = 0.1 # infection limit
#***********END OF USER BLOCK*************
#*****************************************
temp_sus = 0 
temp_death = 0
temp_death_rate = 0
temp_recovered = 0
temp_case = 0
temp_sus_list = [sus]
temp_recovered_list = [recovered]
infected_list = [infected]
time_list = [0]
death_list = [death]
sir_total = 0

data = pd.read_csv("covid_confirmed_Atlanta.csv")
county_names = data[1:11]['County Name']
res = []
column_len = len(data.columns)
hope = data.columns.get_loc("10/31/2020")
for (columnName, columnData) in data.iteritems():
    if data.columns.get_loc(columnName) == hope:
        #print(f"Column Name: {columnName}")
        county_and_case = (columnName, columnData[1:11])
        res.append(county_and_case)
#print(res)
#print(res[0][0])
#print(res[0][1][:11])
for i in range(N):
    temp_sus = (-b) * sus * infected * t # Equation 1 delta S first run
    temp_recovered = k * infected * t # Equation 2
    total = sus + recovered + infected
    sus = sus + temp_sus # Equation 7
    case = 0 # value for day
    temp_case += case # total amount added up
    new_case = case - temp_case
    recov = new_case - days_to_recover
    recovered = recovered + temp_recovered # Equation 8
    if infected > infected_limit:
        temp_death_rate = overload_death_rate # update death rate
        temp_death = temp_recovered * temp_death_rate # death for today w/ overlimit
        death = death + temp_death # updating total death 
    else:
        temp_death = temp_recovered * death_rate # death for today with normal death rate
        death = death + temp_death # updating total death

    new_infected = total - sus - recovered
    infected = new_infected
    temp_sus_list.append(sus)
    temp_recovered_list.append(recovered)
    infected_list.append(infected)
    time_list.append(i * t)
    death_list.append(death)


plt.clf() # clear plot
plt.plot(time_list, temp_sus_list,label="Sus") # x and y axis w/ label
plt.plot(time_list, np.array(temp_recovered_list) - np.array(death_list),label="Recovered") # x and y axis w / label
plt.plot(time_list, infected_list, label="Infected")
plt.plot(time_list, death_list, label="Death")
plt.axhline(infected_limit, color="purple", label="Hospital capacity")
# Set the x axis label of the current axis.
plt.xlabel('Time')
# Set the y axis label of the current axis.
plt.ylabel('Counts')
plt.legend() # Legend for given labels
# Set a title 
plt.title('Georgia Coronavirus Cases') # Set up title
# Display the figure.
plt.show() # Displays plot
