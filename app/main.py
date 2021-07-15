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
def incoming_sms():
    message_sid = request.values.get('MessageSid', None)
    message_status = request.values.get('MessageStatus', None)
    logging.info('SID: {}, Status: {}'.format(message_sid, message_status))
    return ('', 204)

if __name__ == "__main__":
    app.run(debug=True)

    app.run(debug=True)
