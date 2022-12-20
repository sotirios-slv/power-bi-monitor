import win32com.client as win32

def send_email(email_subject, recipient_list, email_body):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)

    recipients = '; '.join(recipient_list)

    mail.subject = email_subject
    mail.To = recipients
    mail.CC = 'salpanis@slv.vic.gov.au'
    mail.HTMLBody = email_body
    mail.Send()

# test_body = """
# Good afternoon, Sotirios    
# """

# send_email('Test2',['salpanis@gmail.com'],test_body)