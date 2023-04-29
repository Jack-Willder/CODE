from twilio.rest import Client

for i in range(10):
    account_sid = "AC835617c075251330c7f353cf04c1af30"
    auth_token = "f357bee29acce68dafac1960696b3207"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Test message - {}".format(i),
        from_="whatsapp:+14155238886",
        to="whatsapp:+917339374704"
    )
    print(message.sid)

# HDvutJywxc8JMJ4siAgTfa
