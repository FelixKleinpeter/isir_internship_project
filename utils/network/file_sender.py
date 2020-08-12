#coding:utf-8

import sys
import stomp

def send_to_greta(file):
    conn = stomp.Connection(auto_content_length=False)
    conn.connect('admin', 'admin', wait=True)
    conn.subscribe(destination='/topic/greta.input.fml', id=1, ack='client-individual')

    f = open(file, "r", encoding='utf8')
    content = f.read()

    conn.send(body=content, destination='/topic/greta.input.fml', content_type='application/xml;charset=utf-8', headers={'correlation-id': '', 'priority': '0', 'type': ''})
    conn.disconnect()
