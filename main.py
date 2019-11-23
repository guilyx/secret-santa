import random
import smtplib, ssl
from email.message import EmailMessage

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


# Send the mail
for elem in list_ppl:
    msg = EmailMessage()
    msg.set_content("Hello " + elem + ", your secret santa is : " + secret_dict[elem])
    msg["Subject"] = "Secret Santa"
    msg["From"] = input("Enter the email you want to send the message from : ")
    msg["To"] = email_dict[elem]
    password_mail = input("Enter the password of the email you want to send the message from : ")
    context=ssl.create_default_context()

    with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
        smtp.starttls(context=context)
        smtp.login(msg["From"], password_mail)
        smtp.send_message(msg)