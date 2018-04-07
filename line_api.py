from linebot import LineBotApi
from linebot.models import TextSendMessage, TemplateSendMessage, ButtonsTemplate, CarouselTemplate, CarouselColumn, \
    PostbackTemplateAction, ConfirmTemplate, ImageSendMessage
from linebot.exceptions import LineBotApiError
import setting

REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'
PUSH_ENDPOINT = 'https://api.line.me/v2/bot/message/push'


# reply messageを送る
def reply_message(reply_token, text):
    line_bot_api = LineBotApi(setting.ACCESS_TOKEN)
    # print(text)
    try:
        if not isinstance(text, (list, tuple)):
            text = [text]
        line_bot_api.reply_message(reply_token, [TextSendMessage(text=t) for t in text])
    except LineBotApiError as e:
        print('error')
        print(e)

def reply_template_confirm(reply_token, text, alt_text, actions):
    line_bot_api = LineBotApi(setting.ACCESS_TOKEN)
    line_bot_api.reply_message(reply_token, [TemplateSendMessage(alt_text=alt_text, template=ConfirmTemplate(text,
        actions=actions
    ))])

def reply_template_button(reply_token, text, alt_text, choices):
    line_bot_api = LineBotApi(setting.ACCESS_TOKEN)
    line_bot_api.reply_message(reply_token, [TemplateSendMessage(alt_text, ButtonsTemplate(text, actions=
    [PostbackTemplateAction(label='{0[0]} {0[1]}'.format(e), data='select {0[0]} {0[1]}'.format(e)) for e in choices]
    ))])


# push messageを送る
def push_message(id, text):
    line_bot_api = LineBotApi(setting.ACCESS_TOKEN)
    # print(text)
    try:
        if not isinstance(text, (list, tuple)):
            text = [text]
        line_bot_api.push_message(id, [TextSendMessage(text=t) for t in text])
    except LineBotApiError as e:
        print('error')
        print(e)

def push_image(id, image_url, image_url_preview):
    line_bot_api = LineBotApi(setting.ACCESS_TOKEN)
    line_bot_api.push_message(id, [ImageSendMessage(original_content_url=image_url, preview_image_url=image_url_preview)])
