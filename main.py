from twilio.rest import Client

account_sid = '[Get from your Twilio Account]'
auth_token = '[Get from your Twilio Account]'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='[Generated from Twilio Account]',
  body='The fact that I can do this now is pretty epic. Damn, I love Python!',
  to='[Your own number for testing]'
)

print(message.sid)
