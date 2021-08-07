import socketio
import tornado

port = 3500

sio = socketio.AsyncServer(async_mode="tornado")
app = tornado.web.Application(
	[
		(r"/", socketio.get_tornado_handler(sio))
	]
)
app.listen(port)

@sio.event
async def connect(sid, environ, auth):
    print('connect ', sid)
	# check auth.token against database

@sio.event
async def disconnect(sid):
    print('disconnect ', sid)

def check_for_changes():
	pass

tornado.ioloop.PeriodicCallback(check_for_changes, 60000).start()
tornado.ioloop.IOLoop.current().start()