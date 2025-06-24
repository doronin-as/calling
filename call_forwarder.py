from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

# Phone number to forward incoming calls to
FORWARD_NUMBER = '+79219025472'

@app.route('/voice', methods=['POST'])
def voice():
    resp = VoiceResponse()
    resp.dial(FORWARD_NUMBER)
    return Response(str(resp), mimetype='text/xml')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
