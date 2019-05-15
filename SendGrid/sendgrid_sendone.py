#!/home/porosya/.local/share/virtualenvs/checkio-VEsvC6M1/bin/checkio --domain=py run sendgrid-sendone

# https://py.checkio.org/mission/sendgrid-sendone/

# To solve this mission you must use theSendGrid API Key(this video will explainhow to create your own API Key). Check out thesePython examples.
# 
# It all starts with your first email. Let’s try to send one.
# 
# Your mission is to create a function that sends a welcome email to a user. The function gets two arguments: email and the name of the user.
# 
# Subject of the email should be "Welcome" and body simply "Hi {name}" ({name} should be replaced by a user's name)
# 
# Input:Two arguments: email and a username.
# 
# Output:None. You should send an email. You don’t need to return anything.
# 
# 
# send_email('a.lyabah@checkio.org', 'oduvan')
# send_email('somebody@gmail.com', 'Some Body')
# 
# END_DESC

import sendgrid
from sendgrid.helpers.mail import Email,  Mail, Content

API_KEY = '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'
SUBJECT = 'Welcome'


sg = sendgrid.SendGridAPIClient(apikey=API_KEY)


def send_email(email, name):
    from_email = Email("test@example.com")
    to_email = Email(email)
    subject = SUBJECT
    BODY = f'Hi {name}'
    content = Content("text/plain", BODY)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())

if __name__ == '__main__':
    #These "asserts" using only for self-checking 
    # and not necessary for auto-testing
    send_email('somebody@gmail.com', 'Some Body')
    print('Done')

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    send_email('somebody@gmail.com', 'Some Body')
    print('Done')