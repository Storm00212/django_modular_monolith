import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_asgi_application()

# asgi configuration for a web socket connection.

# import os
# from django.core.asgi import get_asgi_application
# import socketio

# 1. Set the default Django settings module

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# 2. Initialize the standard Django ASGI application


# django_asgi_app = get_asgi_application()

# 3. Initialize the Socket.IO AsyncServer
# 'async_mode="asgi"' tells the server to look for an ASGI environment


# sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins="*")

# 4. Wrap the Django ASGI app and Socket.IO server into a unified ASGI application
# This routes any traffic hitting '/socket.io/' to Socket.IO, and everything else to Django



# application = socketio.ASGIApp(
    #socketio_server=sio,
    #other_asgi_app=django_asgi_app,
    #socketio_path="/socket.io/"
#)

# 5. Define your Socket.IO event handlers below


# @sio.event
# async def connect(sid, environ):
    # print(f"Client connected: {sid}")
    # await sio.emit("reply", {"message": "Connected successfully!"}, room=sid)

# @sio.event
# async def disconnect(sid):
    # print(f"Client disconnected: {sid}")

# @sio.event
# async def message(sid, data):
    # print(f"Message from {sid}: {data}")
    # Broadcast message to all connected clients
    # await sio.emit("broadcast_message", {"data": data})
