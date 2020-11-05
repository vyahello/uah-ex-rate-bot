from typing import Tuple
from bin.server.core import Server, WebServer
from bin.server.requests import Request, ServerRequest

SERVER: Server = WebServer()
WELCOME_MESSAGE: str = "<h1>Welcome to UAH rate telegram bot home page</h1>"
METHODS: Tuple[str, ...] = ("POST", "GET")
POST: str = "POST"

from . import routes
