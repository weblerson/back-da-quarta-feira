from fastapi import FastAPI, Request
from pydantic import BaseModel
from decouple import config

from typing import List

__all__: List[str] = ['Config', 'FastAPI', 'Request', 'GlobalArea']


class Config:
    def __init__(self) -> None:
        self.__app: FastAPI
        if config('PROD', cast=bool, default=True):
            self.__app = FastAPI()
        else:
            self.__app = FastAPI(docs_url=None, redoc_url=None)

    @property
    def app(self) -> FastAPI:
        return self.__app


class GlobalArea(BaseModel):
    region: str
