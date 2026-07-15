from dnd.server.app import create_app
from mangum import Mangum

handler = Mangum(create_app())
