from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import time

app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a MMS message."""
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a text message
    msg = resp.message("The Robots are coming! Head for the hills!")
    time.sleep(2)
    msg = resp.message("... it's too late- they got me!")
    time.sleep(10)

    # Add a picture message
    msg.media("https://farm8.staticflickr.com/7090/6941316406_80b4d6d50e_z_d.jpg")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
