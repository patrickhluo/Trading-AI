import imaplib
import email
from email.header import decode_header
import webbrowser
import os
import datetime


def within_5(direction,emailtime):
    current_time = datetime.datetime.now()
    
    direction = direction
    time = emailtime
    email_year = time[0:4]
    email_month = time[5:7]
    email_day = time[8:10]
    email_hour = time[11:13]
    email_minute = time[14:16]
    email_sec = time[17:19]
    email_time = datetime.datetime(int(email_year),int(email_month),int(email_day),int(email_hour),int(email_minute),int(email_sec))
    delta_4 = datetime.timedelta(hours= 4)
    email_time = email_time-delta_4
    #deterimine if the email is received within 5 min
    t5delta = datetime.timedelta(minutes=5)
    if current_time-t5delta<email_time<current_time+t5delta:
        return True
    else:
        return False


# account credentials
username = ##enter your credential
password = ##enter your credential
# create an IMAP4 class with SSL 
imap = imaplib.IMAP4_SSL("outlook.office365.com")
# authenticate
imap.login(username, password)
status, messages = imap.select("INBOX")
# number of top emails to fetch
N = 3
order = False
# total number of emails
# Error Test
try: 
    messages = int(messages[0])
except Exception as e:
    f = open('Error_Log','r+')
    f_lines = f.readlines()
    f.write(e)
    f.close()
    exec(open('CheckEmail.py').read())
for i in range(messages, messages-N, -1):
    # fetch the email message by ID
    res, msg = imap.fetch(str(i), "(RFC822)")
    for response in msg:
        if isinstance(response, tuple):
            # parse a bytes email into a message object
            msg = email.message_from_bytes(response[1])
            # decode the email subject
            subject = decode_header(msg["Subject"])[0][0]
            if isinstance(subject, bytes):
                # if it's a bytes, decode to str
                subject = subject.decode()
            # email sender
            from_ = msg.get("From")

            # print(subject.split()[-1])
            # print("From:", from_)

            #Tradingview email filter
            if from_.split()[0] == 'TradingView':
                # print(subject.split()[-1])
                print(subject)


                direction = subject.split()[-4]
                emailtime = subject.split()[-3]
                open_price = subject.split()[-2]
                close_price = subject.split()[-1]
                found = False
                f = open('Alert','r+')
                for line in f.readlines():
                    fi = open('Full_Log','r+')
                    fi_lines = fi.readlines()
                    fi.write(line+'\n')
                    fi.close()
                    print(line)
                    if line.split()[0]==direction and line.split()[1]==emailtime:
                        found = True
                if not found:
                    email_info = direction+' '+emailtime+' '+open_price +'  ' + close_price + '\n'
                    f.write(email_info)
                    order=True
                    fi = open('Full_Log','r+')
                    fi_lines = fi.readlines()
                    fi.write(email_info+'\n')
                    fi.close()
                f.close()
                # print(direction,emailtime)
                # if within_5(direction,emailtime) :
                #     sending = True
                #     print('Subject:',subject)

            # what = input()
            # if what == 'In':
            #     file_object.write('In')
            #     print('In')
            # else:
            #     file_object.write('Out')
            #     print('Out')
            # if file_object.read()=='In':
            #     file_object.write('Out')
            # file_object.write('In')

            # if the email message is multipart
            # if msg.is_multipart():
            #     # iterate over email parts
            #     for part in msg.walk():
            #         # extract content type of email
            #         content_type = part.get_content_type()
            #         content_disposition = str(part.get("Content-Disposition"))
            #         try:
            #             # get the email body
            #             body = part.get_payload(decode=True).decode()
            #         except:
            #             pass
            #         if content_type == "text/plain" and "attachment" not in content_disposition:
            #             # print text/plain emails and skip attachments
            #             print(body)
            #         elif "attachment" in content_disposition:
            #             # download attachment
            #             filename = part.get_filename()
            #             if filename:
            #                 if not os.path.isdir(subject):
            #                     # make a folder for this email (named after the subject)
            #                     os.mkdir(subject)
            #                 filepath = os.path.join(subject, filename)
            #                 # download attachment and save it
            #                 open(filepath, "wb").write(part.get_payload(decode=True))
            # else:
            #     # extract content type of email
            #     content_type = msg.get_content_type()
            #     # get the email body
            #     body = msg.get_payload(decode=True).decode()
            #     if content_type == "text/plain":
            #         # print only text email parts
            #         print(body)
            # if content_type == "text/html":
            #     # if it's HTML, create a new HTML file and open it in browser
            #     if not os.path.isdir(subject):
            #         # make a folder for this email (named after the subject)
            #         os.mkdir(subject)
            #     filename = f"{subject[:50]}.html"
            #     filepath = os.path.join(subject, filename)
            #     # write the file
            #     open(filepath, "w").write(body)
            #     # open in the default browser
            #     webbrowser.open(filepath)
            # print("="*100)
imap.close()
imap.logout()
# os.system('xset dpms force off')

if order:           
    print('order creating')

    f = open('Log','r+')
    f.readlines()
    f.write('order creating %s '%(email_info))
    f.close()

    exec(open('BinanceOrder.py').read())

    fi = open('Full_Log','r+')
    fi_lines = fi.readlines()
    fi.write('order creating'+'\n')
    fi.close()
    




