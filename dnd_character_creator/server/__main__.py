import uvicorn
from dnd_character_creator.server.app import app

if __name__ == "__main__":
    uvicorn.run(app)
