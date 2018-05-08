# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
from reply import reply
from receive import receive
import web

import traceback
from textMsgHandle import textmsghandle

class Handle(object):
    def POST(self):
        try:
            webData = web.data()
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName

                if recMsg.MsgType == 'text':
                    return textmsghandle(toUser,fromUser,recMsg)
                    
                if recMsg.MsgType == 'image':
                    mediaId = recMsg.MediaId
                    replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    return replyMsg.send()
                else:
                    return reply.Msg().send()
            else:
                print "暂且不处理"
                return reply.Msg().send()
        except Exception, Argment:
            print repr(Argment)
            traceback.print_exc()