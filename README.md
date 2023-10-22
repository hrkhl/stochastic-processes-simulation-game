# stochastic-processes-simulation-game
simulate a simple game where 30 players roll a die 300 times and keep track of their rolls. The game ends when all players have the same number.

The game starts with 30 players, each of whom chooses a random number between 1 and 10.
A die is rolled 300 times, and the results are recorded.
Each player enters the game at the step corresponding to their chosen number. For example, if a player chooses 5, they look at the fifth number in the list of rolls and record it.
The player then rolls the die and adds the result to their current number. They then record this new number.
This process continues until all players have the same number.

The question is: how many steps does it take for all players to reach the same number? The answer depends on the random numbers that the players choose and the results of the die rolls. Therefore, to find the exact answer, you must simulate the game and record the results.
