# -*- coding: utf-8 -*-
import jieba
import jieba.posseg as psg
from dboperation.dbsession import session
from dboperation.readop import ReadOperation
from reply import reply


def textmsghandle(toUser,fromUser,recMsg):
    '''处理文本消息'''
    if recMsg.Content.startswith('分词:'):
        replyText=''
        #print type(recMsg.Content)    # str

        for x in psg.cut(recMsg.Content.decode('utf8')[3:].encode('utf8')):
            #print type(x.word)   # unicode
            replyText+=x.word.encode("utf8")
            replyText+=x.flag.encode("utf8")
        replyMsg = reply.TextMsg(toUser, fromUser, replyText)
        return replyMsg.send()

    r=[]
    for x in psg.cut(recMsg.Content):
        if x.flag=='nr':
            r.append(x.word)
    with session.begin_transaction() as tx:
        result=ReadOperation.read_common_course(tx,*r)
        replyList=[]
        for i in result:
            replyList.append(i.values()[0].properties['kcmc'].encode("utf8"))
        replyText="\n".join(replyList)
        replyMsg = reply.TextMsg(toUser, fromUser, replyText)
        tx.commit()
        return replyMsg.send()