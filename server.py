from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from battleship import Battleship

app = Flask(__name__)
game = Battleship()


@app.route("/", methods=['POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    print('BODY: ', body)
    # Start our TwiML response
#    resp = MessagingResponse(to='+4917657643201')
    # Determine the right reply for this message
    try:
        resp = (game.turn(request.values.get('From'), body))
    #finally:
    except:
        resp = 'Please specify coordinates in format <A-J, 1-10>.'
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
