from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import time

app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply1():
    """Respond to incoming calls with a MMS message."""
    # Start our TwiML response
    resp = MessagingResponse()
    # Add a text message
    msg = resp.message("The Robots are coming! Head for the hills!")
    return str(resp)

def sms_reply2():
    resp=MessagingResponse()
    msg = resp.message("... it's too late- they got me!")
    return str(resp)

def sms_reply3():
    resp=MessagingResponse()
    # Add a picture message
    msg.media("https://farm8.staticflickr.com/7090/6941316406_80b4d6d50e_z_d.jpg")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
