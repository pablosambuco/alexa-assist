#!/usr/bin/python3
"""api.py: API para el tratamiento de mensajes de Alexa."""

# pylint: disable=line-too-long,fixme,E1101,no-name-in-module

import os
import time
from pathlib import Path
import logging
import json
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
    """Clase para interpretar los mensajes del POST"""
    text: str

APP = FastAPI()

@APP.post("/")
async def read_post(message: Message):
    """Tratamiento del POST"""
    req = json.loads(message.text)
    accion = req.keys()[0]
    contenido = req.values()[0]
    respuesta = ""
    if accion=="log":
        LOGGER.info(msg=contenido)
        respuesta = "log ok"
    elif accion == "get":
        if contenido == "time":
            respuesta = time.srtftime("%H:%M",time.localtime())
            LOGGER.info(msg="get time")
    return respuesta


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
