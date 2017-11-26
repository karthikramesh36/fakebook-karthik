import time
import boto3
from flask import current_app

"""find the current time to store it as image file name so that each file
    has a different name and can be differentiated through time"""
def utc_now_ts():
    return int(time.time())
    
""" function to send out emails from AWS ses from authorized admin account"""

def email(to_email, subject, body_html, body_text):
    if current_app.config.get('TESTING') or not current_app.config.get('AWS_SEND_MAIL'):
        return False
        
    client = boto3.client('ses',region_name='us-west-2')
    return client.send_email(
        Source='karthk.floyd@gmail.com',
            Destination={
                'ToAddresses': [
                    to_email,
                ]
            },
        Message={
            'Subject': {
                'Data': subject,
                'Charset': 'UTF-8'
            },
            'Body': {
                'Text': {
                    'Data': body_text,
                    'Charset': 'UTF-8'
                },
                'Html': {
                    'Data': body_html,
                    'Charset': 'UTF-8'
                },                
            }
        }
    )    