from socketio.namespace import BaseNamespace
from socketio.mixins import BroadcastMixin


class EventNamespace(BaseNamespace, BroadcastMixin):
    def on_keyEvent(self, msg):  
        #print 'ggggggggggggg'+msg['id']
        #self.emit('gg', { 'hello': 'world' })
        self.broadcast_event('keyEvent', {'key': msg['key']})






