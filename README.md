# Calling

This repository contains a simple example of a call forwarding service using [Twilio](https://www.twilio.com/) and Flask.

## Prerequisites

- Python 3.7+
- A Twilio account with a purchased phone number

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Set up your Twilio phone number's voice webhook to point to `/voice` on your server. For local testing you can use a tool like ngrok to expose your Flask app.

Run the server:

```bash
python call_forwarder.py
```

When someone calls your Twilio number, the call will be forwarded to the configured number in `call_forwarder.py`.
