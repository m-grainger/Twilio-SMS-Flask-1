from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("The Robots are coming! Head for the hills!")

    return str(resp)
    # a message comes in webhook default page below
    # https://demo.twilio.com/welcome/sms/reply/
    
    # Add a picture
    msg.media("https://farm8.staticflickr.com/7090/6941316406_80b4d6d50e_z_d.jpg")

if __name__ == "__main__":
    app.run(debug=True)
    
    
