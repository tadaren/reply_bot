from bottle import *
import setting
from linebot import webhook
import json
import line_api
import os
import re
import db

reply = {}

@post('/line_bot')
def line_bot():
    signature = request.get_header('X-Line-Signature')
    body = request.body.read().decode('utf-8')

    events = webhook.WebhookParser(setting.CHANNEL_SECRET).parse(body, signature)
    main(events)

    body = json.dumps({})
    r = HTTPResponse(status=200, body=body)
    r.set_header('Content-Type', 'application/json')


def main(events):
    for event in events:
        event_dict = event.as_json_dict()
        event_type = event.type
        if event_type == 'message':
            message(event_dict)


def message(event):
    if event['message']['type'] != 'text':
        return
    text = event['message']['text'].split()
    reply_token = event['replyToken']
    if len(text) >= 3 and text[1] in ['->', '=', '==', '＝']:
        db.insert(text[0], text[2])
        line_api.reply_message(reply_token, 'success')
        return
    # text2 = text[0].split('=')
    text2 = re.split(r'[=＝]', event['message']['text'])
    if len(text2) >= 2:
        db.insert(text2[0], text2[1])
        line_api.reply_message(reply_token, 'success')
        return
    reply = db.get_all()
    if text[0] in reply:
        line_api.reply_message(reply_token, reply[text[0]])
        return
    

run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))