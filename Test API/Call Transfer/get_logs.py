from twilio.rest import Client

# To find these visit https://www.twilio.com/user/account
account_sid = "AC15ff1d6e4703e28ac88b82431f2c9bb5"
auth_token = "9ce0f253df11958e93943ab9ad319fb9"

client = Client(account_sid, auth_token)

for call in client.api.account.calls.list():
    print("From: " + call.from_formatted + " To: " + call.to_formatted)