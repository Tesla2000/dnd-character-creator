from dnd_character_creator.server.app import app
from mangum import Mangum

handler = Mangum(app)
