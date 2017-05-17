from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather

app = Flask(__name__)

# Handle incoming voice call
@app.route('/incoming', methods=['GET', 'POST'])
def voice():
    twiml = VoiceResponse()
    gather = Gather(action='/callback',
     timeout='3',
     input='speech',
     partial_result_callback='/partial')
    gather.say('Welcome to Signal Air, where can we take you?')
    twiml.append(gather)
    return str(twiml)

# Handle POST from <Gather> action read out final result
@app.route('/callback', methods=['GET', 'POST'])
def callback():
    speech_result = request.values.get('SpeechResult', None)
    print 'SpeechResult: ' + speech_result
    twiml = VoiceResponse()
    twiml.say('You said ' + speech_result)
    return str(twiml)

# Handle POST from <Gather> partialResultCallback and print intermediate results
@app.route('/partial', methods=['GET', 'POST'])
def partial():
    print 'SequenceNumber: ' + request.values.get('SequenceNumber', None)
    print 'UnstableSpeechResult: ' + request.values.get('UnstableSpeechResult', None)
    print 'StableSpeechResult: ' + request.values.get('StableSpeechResult', None)
    return 'OK'

if __name__ == '__main__':
    app.run(port=9393, debug=True)