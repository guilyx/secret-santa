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

email_dict = dict()
for elem in list_ppl:
    email_dict[elem] = input("Enter " + elem + "'s EMAIL --> ")

secret_dict = dict()
list_match = list_ppl.copy()
for elem in list_ppl:
    secret_santa = random.choice(list_match)
    secret_dict[elem] = secret_santa
    list_match.remove(secret_santa)

print(secret_dict)
print(email_dict)

# Email handle #

sender = 'secretsanta.test1996@gmail.com'


sender = "secretsanta.test1996@gmail.com"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

#Next, log in to the server
server.login("secretsanta.test1996@gmail.com", "flifel85")

#Send the mail
for elem in list_ppl:
    msg = """
    Hey """ + elem + """, your secret santa is : """ 
    + secret_dict[elem] 
    server.sendmail(sender, email_dict[elem], msg)

server.quit()