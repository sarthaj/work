# Download the library from twilio.com/docs/libraries
from twilio.rest import Client

# Get these credentials from http://twilio.com/user/account
account_sid = "AC15ff1d6e4703e28ac88b82431f2c9bb5"
auth_token = "9ce0f253df11958e93943ab9ad319fb9"
client = Client(account_sid, auth_token)


# Make the call
call = client.api.account.calls\
	  .create(to="+919567333696",  # Any phone number
	          from_="+16782288028", # Must be a valid Twilio number
	          url="http://e6845669.ngrok.io")

print(call.sid)