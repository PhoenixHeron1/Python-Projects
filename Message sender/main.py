import os
from twilio.rest import Client

account_sid = "AC0c41ba7ba1a9e5b122148b4b1b3c31a4"
auth_token = "0954f26e1132495a124e9b916b9496cf"

client = Client(account_sid, auth_token)

message = client.messages \
    .create(
        body='This is the ship that made the Kessel Run in fourteen parsecs?',
        from_='+17577808855',
        to='+919417537826'
    )

print(message.sid)

