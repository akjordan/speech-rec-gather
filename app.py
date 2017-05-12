from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import abort, Flask, request

from twilio.twiml.voice_response import VoiceResponse, Gather

# Declare and configure application
app = Flask(__name__, static_url_path='/static')
app.config.from_pyfile('local_settings.py')

# Handle incoming voice call
@app.route('/incoming', methods=['GET', 'POST'])
def voice():
    twiml = VoiceResponse()
    twiml.say("Hello, welcome to Twilio ASR.")
    gather = Gather(action="/callback",
     timeout="2",
     input="speech",
     partial_result_callback="/partial")
    gather.say("Please tell us why you're calling.")
    gather.pause(length="2")
    twiml.append(gather)
    return str(twiml)

# Handle POST from <Gather> action read out final result
@app.route('/callback', methods=['GET', 'POST'])
def callback():
    twiml = VoiceResponse()
    twiml.say("You said" + request.values.get('SpeechResult', None))
    return str(twiml)

# Handle POST from <Gather> partialResultCallback print intermediate results
@app.route('/partial', methods=['GET', 'POST'])
def partial():
    print "SequenceNumber: " + request.values.get('SequenceNumber', None)
    print "UnstableSpeechResult: " + request.values.get('UnstableSpeechResult', None)
    print "StableSpeechResult: " + request.values.get('StableSpeechResult', None)
    return "OK"

if __name__ == '__main__':
    app.run(port=9393, debug=True)