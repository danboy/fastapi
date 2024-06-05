#inspiration from https://github.com/mirzadelic/fastapi-starter-project
from dotenv import load_dotenv
from fastapi import FastAPI

from routes import items, ping, root

load_dotenv()

app = FastAPI()

app.include_router(root.router)
app.include_router(items.router)
app.include_router(ping.router)
