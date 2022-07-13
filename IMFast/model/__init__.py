"""
If you want to make appmodel code, I suggest jsonable_encoder
"""
from fastapi import FastAPI
from settings import Settings
from model.mongodb import get_client
# from model.mongodb.initializer import ...


def init_app(app: FastAPI, setting: Settings):
    """"Model init"""
    # TODO IML Author append here

