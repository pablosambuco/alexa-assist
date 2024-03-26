import os
from pathlib import Path
import logging
from logging.handlers import RotatingFileHandler
from fastapi import FastAPI
from pydantic import BaseModel

DIRNAME = os.path.dirname(os.path.realpath(__file__))
Path("logs").mkdir(parents=True, exist_ok=True)
LOGGER = logging.getLogger()
HANDLER = RotatingFileHandler(os.path.join(DIRNAME,"logs/web.log"), maxBytes=1024**2, backupCount=5)
FORMATTER = logging.Formatter("%(levelname)s %(asctime)s %(message)s")
HANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(HANDLER)
LOGGER.setLevel(logging.INFO)


class Message(BaseModel):
    text: str

APP = FastAPI()

@APP.post("/")
async def read_post(message: Message):
    LOGGER.info(msg=message.text)
    return message


@APP.get("/{anything}")
async def read_get(anything: str = None):
    LOGGER.info(msg=anything)
    return {}


def get_interface():
    """Obtiene la interfaz donde debe levantarse el servidor."""
    interface = 0
    if os.path.exists("interface.cfg"):
        with open("interface.cfg", encoding="utf-8") as ifacefile:
            interface = ifacefile.read()
    return interface


def get_port():
    """Obtiene el puerto donde debe levantarse el servidor."""
    port = 0
    if os.path.exists("port.cfg"):
        with open("port.cfg", encoding="utf-8") as portfile:
            port = int(portfile.read())
    return port
