# Import libraries
import numpy as np

# Set game parameters
n = 30 # Number of players
m = 300 # Number of dice rolls

# Generate random choices for each player
choices = np.random.randint(1, 11, n)

print ('Choices:\n' , choices)

# Roll the dice m times and store the results in a list
dice = np.random.randint(1,7,m)

# Initialize an empty list to store the numbers for each player
numbers = []

# Loop over the players
for i in range(n):

  # Initialize a list with a default value of zero for the current player
  player_numbers = [0]

  # Append the player's list to the numbers list
  numbers.append(player_numbers)

# Initialize an empty list to store the mean numbers for each step
mean_numbers = []

# Initialize a variable to store the step where the numbers become equal
equal_step = None

# Loop over the dice rolls
for j in range(m):

  # Initialize an empty list to store the numbers for each player at the current step
  step_nums = []

  # Loop over the players
  for i in range(n):

    # Check if the current index matches the start index
    if j == choices[i] - 1:

      # Append the dice number to the player's list
      numbers[i].append(dice[j])

      # Update the start index by adding the dice number
      choices[i] += dice[j]

    # Append the last number of the player's list to the step list
    step_nums.append(numbers[i][-1])

  # Calculate and append the mean of the numbers at the current step
  mean_numbers.append(np.mean(step_nums))

  # Check if all the numbers are equal and equal_step is not set yet
  if len(set(step_nums)) == 1 and equal_step is None:

    # Set the equal step to be the current step
    equal_step = j

# Print the results
#print("Choices:", choices)
print("Dice:", dice)
#print("Numbers:", numbers)
#print("Mean Numbers:", mean_numbers)
if equal_step is not None:
  print("The numbers become equal at step", equal_step + 1)
else:
  print("The numbers do not become equal in", m, "steps")
