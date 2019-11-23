import numpy
import random
import smtplib

# Ask how many people participate
# According to this, store N people's names
# Assign to each person another person randomly

# Secret Santa definition #

nb_ppl = int(input("How many people are participating to the Secret Santa ? --> "))
list_ppl = []
for i in range(nb_ppl):
    list_ppl.append(input("Enter person number " + str(i+1) + "'s name --> "))

secret_dict = dict()
list_match = list_ppl.copy()
for elem in list_ppl:
    secret_santa = random.choice(list_match)
    secret_dict[elem] = secret_santa
    list_match.remove(secret_santa)

print(secret_dict)

# Email handle #

sender = 