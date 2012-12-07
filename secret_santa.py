#!/usr/bin/python

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
from random import shuffle
import os
import sys

gmail_user = "unul_dintre_cele_mai_importante_e-mail-uri_evaaa"
gmail_pwd = "importanta_mea_parola"

def mail(to, subject, text):
   msg = MIMEMultipart()

   msg['From'] = gmail_user
   msg['To'] = to
   msg['Subject'] = subject

   msg.attach(MIMEText(text))

   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(gmail_user, gmail_pwd)
   mailServer.sendmail(gmail_user, to, msg.as_string())
   # Should be mailServer.quit(), but that crashes...
   mailServer.close()

givers = [line.strip().split(',') for line in sys.stdin]
givers = [(name.strip(), email.strip()) for name, email in givers]

shuffle(givers)

print len(givers)

for x in range(0, len(givers) - 1):
    first = givers[x]
    second = givers[x+1]
    print first[0]
    print second[0]

    hello = "Ciaules %s" % first[0]
    email = first[1]
    mail(email, 
        hello, 
        "Ti-a fost asignata urmatoarea persoana pentru secret santa: %s (mesaj trimis de masina)"%second[0])

print givers[len(givers) - 1][0]
print givers[0][0]

hello = "Ciaules %s" % givers[len(givers) - 1][0]
email = givers[len(givers) - 1][1]
mail(email, 
        hello, 
        "Ti-a fost asignata urmatoarea persoana pentru secret santa: %s (mesaj trimis de masina)"%givers[0][0])