Question:
Given two 1D arrays, birds and age, where each bird has a corresponding age, return the bird names sorted in ascending order based on their ages.
Code:
import numpy as np
birds = np.array([
    'spoonbills', 'plovers', 'plovers', 'plovers', 'plovers',
    'Cranes', 'plovers', 'plovers', 'Cranes', 'spoonbills'
])

age = np.array([
    5.5, 6.0, 3.5, 1.5, 3.0,
    4.0, 3.5, 2.0, 5.5, 6.0
])

print("Birds:")
print(birds)

print("\nAge:")
print(age)

index = np.argsort(age)

print("\nSorted Indices:")
print(index)
sorted_birds = birds[index]

print("\nBirds Sorted by Age:")
print(sorted_birds)
