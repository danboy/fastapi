from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send(message):
    message = Mail(
        from_email='no-reply@leapinc.co',
        to_emails=message.recipients,
        subject='Sending with Twilio SendGrid is Fun',
        html_content=message.body)
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        return response
    except Exception as e:
        return { 'exception': e, 'key': os.environ.get('SENDGRID_API_KEY')  }

