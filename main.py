from server.instance import Server

from controllers import *

from werkzeug.utils import cached_property
from werkzeug.local import ContextVar

Server.run()
    
