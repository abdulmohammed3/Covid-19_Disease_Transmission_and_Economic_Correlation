import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# k = how fast recovered b = how fast infected
#****************************************
#************START OF USER BLOCK*********
b = 0.5 
k = 0.33
recovered = 0.
infected = 0.00000127
sus = 1.
t = 0.1 # delta T
N = 1000 # Time steps
#***********END OF USER BLOCK*************
#*****************************************
temp_sus = 0
temp_recovered = 0
temp_sus_list = [sus]
temp_recovered_list = [recovered]
infected_list = [infected]
time_list = [0]
sir_total = 0

for i in range(N):
    temp_sus = (-b) * sus * infected * t # Equation 1 delta S first run
    temp_recovered = k * infected * t # Equation 2
    total = sus + recovered + infected
    sus = sus + temp_sus # Equation 7
    recovered = recovered + temp_recovered # Equation 8
    new_infected = total - sus - recovered
    infected = new_infected
    temp_sus_list.append(sus)
    temp_recovered_list.append(recovered)
    infected_list.append(infected)
    time_list.append(i * t)

plt.clf() # clear plot
plt.plot(time_list, temp_sus_list,label="Sus") # x and y axis w/ label
plt.plot(time_list, temp_recovered_list,label="Recovered") # x and y axis w / label
plt.plot(time_list, infected_list, label="Infected")
# Set the x axis label of the current axis.
plt.xlabel('Time')
# Set the y axis label of the current axis.
plt.ylabel('Counts')
plt.legend() # Legend for given labels
# Set a title 
plt.title('Georgia Coronavirus Cases') # Set up title
# Display the figure.
plt.show() # Displays plot