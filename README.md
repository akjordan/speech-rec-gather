# speech-rec-gather

To get started, you need a Twilio account, ngrok, pip and venv.

Clone this repo and navigate to the folder and run `source asr_demo/bin/activate`

This should put you in a venv with all the dependencies you need.

Next run python `app.py` to start the application, I have the port set to 9393, you may want to change it to 8080.

Start ngrok with `ngrok http -subdomain=myasrdemo 9393` using a custom subdomain will make your life much easier.

Buy a number from Twilio and configure the Voice URL to point to `http://myasrdemo.ngrok.io/incoming`

Call that Twilio number to interact with the demo.
