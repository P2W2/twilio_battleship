# Battleship Game
This is a battleship game with the Twilio API. It is a simple app to get to know Twilio.\
It is based on the Twilio Tutorial: [Receive and Reply to SMS and MMS Messages in Python](https://www.twilio.com/docs/sms/tutorials/how-to-receive-and-reply-python)


# Get Started

Make a Twilio Account and get a [number](https://www.twilio.com/console/phone-numbers/search).\
Deploy the docker container or the Flask app on your server.\
Start the Flask app via:\
```python3 server.py <HOST> <PORT>```\
OR\
Start the Docker container via:\
```docker build -t battleship .```\
```docker run battleship <HOST> <PORT>```

Next, configure Your Webhook URL:
1. Log into Twilio.com and go to the  [Console's Numbers page](https://www.twilio.com/console/phone-numbers/incoming)
2. Click on the phone number you'd like to modify
3. Find the Messaging section and the "A MESSAGE COMES IN" option
4. Select "Webhook" and paste in the URL you want to use

Now send an SMS to the Twilio number with the content:\
```A, 1```

HAVE FUN
