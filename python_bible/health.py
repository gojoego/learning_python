# importing modules are always done at the top of the script 
import random
# yellow text for import designates important key word 

# create variable called health with 50 assigned to it 
health = 50

# define variable called difficulty - less and less healthy at higher difficulties
# 1 easy, 2 medium, 3 hard 
difficulty = 3 

# create variable called potion_health with random number between 25 and 50
# use random.randint()

potion_health = int(random.randint(25,50) / difficulty)

health = health + potion_health

print(health)

# use variables to represent real life concepts
