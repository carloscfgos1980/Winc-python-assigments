# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# PART I
# Dutch goal scorers
goal_scorer_0 = 'Ruud Gullit'
goal_scorer_1 = 'Marco Van Basten'

# Netherlands scored twice againts URSS. This was the exact time that happened!
goal_0 = 32
goal_1 = 54


# Goals report
scorers = goal_scorer_0 + ' ' + \
    str(goal_0) + ',' + ' ' + goal_scorer_1 + ' ' + str(goal_1)
print(scorers)
# Report
report = f'{goal_scorer_0} scored in the {goal_0}nd minute\n{goal_scorer_1} scored in the {goal_1}nd minute'

print(report)

# PART II

player = 'Gut Von Examplestein'  # Name of the goal scorer

first_name = player[:player.find(' ')]  # First name
print(first_name)


last_name_index = player.find(' ') + 1 # if I don't add 1, then the blanck space is also considered
print(last_name_index)

last_name = player[last_name_index:]  # Last name
print(last_name)

name_short = f'{player[0]}. {last_name}'
print(name_short)

chant = f'{first_name}!\t' * 3
print(chant)

print(chant[-1] != ' ')  # (-1) returns the last index number of the string
