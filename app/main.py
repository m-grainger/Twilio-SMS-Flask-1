from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import logging

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a MMS message."""
    # Start our TwiML response
    resp = MessagingResponse()
    # Add a text message
    msg = resp.message(f"TwilioQuest rules")
    # Add a picture message
    msg.media("https://farm8.staticflickr.com/7090/6941316406_80b4d6d50e_z_d.jpg")

    return str(resp)

@app.route("/MessageStatus", methods=['POST'])
def my_status_function():
    print(f"Message SID {request.values.get('MessageSid')} has a status of {request.values.get('MessageStatus')}")

if __name__ == "__main__":
    app.run(debug=True)

    app.run(debug=True)
