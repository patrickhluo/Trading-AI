import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



f = open('Alert','r')
lines = f.readlines()
line = lines[-1]
direction = line.split()[0]
email_time = line.split()[1]
open_price = line.split()[2]
close_price = line.split()[3]



sender_email = ##enter your credential
receiver_email = ##enter your credential
password = input("Type your password and press enter:")
# password = ##enter your credential

message = MIMEMultipart("alternative")
message["From"] = sender_email
message["To"] = receiver_email

#subjects
# message["Subject"] = "Alert In"
# if Status:
#   message["Subject"] = "Success"

message["Subject"] = "Alert has triggered"

# Create the plain-text and HTML version of your message


text = """\
Alert has triggered
"""
html = """\
<html>
  <body>
    <p><br>
       Alert has triggered
       Alert is %s
       Time is %s
       Open price is %s
       Close price is %s
       <br>
    
    </p>
  </body>
</html>
"""%(direction,email_time,open_price,close_price)

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )


print("Email Sent")

f = open('Log','r+')
lines = f.readlines()
f.write('Email Sent \n')
f.close()

fi = open('Full_Log','r+')
fi_lines = fi.readlines()
fi.write('Email Sent \n')
fi.close()
