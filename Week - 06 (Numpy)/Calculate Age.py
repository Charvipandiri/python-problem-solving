Question:
Given a list of birds and their corresponding age, calculate the mean age of the Crane bird (rounded off to 2 decimal points)
Code:
import numpy as np
birds = ['spoonbills', 'plovers', 'plovers', 'plovers', 'plovers',
         'Cranes', 'plovers', 'plovers', 'Cranes', 'spoonbills']
age = [5.5, 6.0, 3.5, 1.5, 3.0,
       4.0, 3.5, 2.0, 5.5, 6.0]

def calculate_mean_age(birds, age):
    birds = np.array(birds)
    age = np.array(age)
    mask =(birds == "Cranes")
    crane_ages = age[mask]
    mean_age = np.mean(crane_ages)
    mean_age = np.round(mean_age, 2)

    return mean_age

result = calculate_mean_age(birds, age)
print("Mean Age of Crane Birds:", result)
