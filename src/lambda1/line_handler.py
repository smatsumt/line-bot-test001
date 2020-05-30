#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import (
    MessageEvent, TextMessage, ImageMessage, LocationMessage, TextSendMessage,
)

line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN', 'YOUR_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('LINE_CHANNEL_SECRET', 'YOUR_CHANNEL_SECRET'))

logger = logging.getLogger(__name__)


def callback(headers, body):
    # get X-Line-Signature header value
    signature = headers['X-Line-Signature']

    # get request body as text
    logger.info("Request body: " + body)

    # handle webhook body
    handler.handle(body, signature)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    """ TextMessage handler """
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


@handler.add(MessageEvent, message=ImageMessage)
def handle_message(event):
    """ ImageMessage handler """
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.id))


@handler.add(MessageEvent, message=LocationMessage)
def handle_message(event):
    """ LocationMessage handler """
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.address))
