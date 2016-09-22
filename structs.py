#!/usr/bin/env python
# -*- coding: utf-8 -*-

def text_message(recipient_id, message_text):
    message_data = {
        'recipient': {'id': recipient_id},
        'message': { 'text': message_text}
    }
    return message_data

def typing_message(recipient_id):
    message_data = {
        'recipient': {'id': recipient_id},
        'sender_action' : 'typing_on'
    }
    return message_data

def quick_replie_message(recipient_id, title, replies ):
    message_data = {
        'recipient': {'id': recipient_id},
        'message': {    
            'text': title,
            'quick_replies': replies
        }
    }
    return message_data

def item_quick_replie(title, payload):
    data =  {
			"content_type":"text",
			"title": title,
			"payload": payload
		  }
    return data

def quick_replies_location(title, recipient_id):
    message_data = {
        'recipient': {'id': recipient_id},
        'message': {    
            'text': title,
            "quick_replies":[
              {
                "content_type":"location",
              }
            ]
        }
    }
    return message_data

""" Funciones Para crear las estructuras """
def create_quick_replies_message(data, user):
    replies = []
    for replie in data['replies']:
        item = item_quick_replie(replie['title'], replie['payload'])
        replies.append( item  )
    
    return quick_replie_message( user['user_id'], data['content'], replies)

def create_text_message(data, user, data_model):
    message = data.get('content', '')
    if 'format' in data:
        message = message.format(**user)
    return text_message(user['user_id'], message)

def create_quick_replies_location(data, user):
    return quick_replies_location(data['title'], user['user_id'])

