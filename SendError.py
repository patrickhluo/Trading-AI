import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



f = open('Error_log','r')
lines = f.readlines()
line = lines[-1]




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

message["Subject"] = "Error has occured"

# Create the plain-text and HTML version of your message


text = """\
Error has occured
"""
html = """\
<html>
  <body>
    <p><br>
       Error message is %s
       <br>
    
    </p>
  </body>
</html>
"""%(e)

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


      #  <a href="http://www.realpython.com">Real Python</a> 
      #  has many great tutorials.
  # (line 37)

print("Error Email Sent")

f = open('Log','r+')
lines = f.readlines()
f.write('Error Email Sent \n')
f.close()

fi = open('Full_Log','r+')
fi_lines = fi.readlines()
fi.write('Error Email Sent \n')
fi.close()
