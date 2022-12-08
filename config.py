from fastapi import FastAPI
from decouple import config

from typing import List

__all__: List[str, ...] = ['Config', 'FastAPI']


class Config:
    def __init__(self) -> None:
        self.__app: FastAPI
        if config('PROD', cast=bool, default=False):
            self.__app = FastAPI()
        else:
            self.__app = FastAPI(docs_url=None, redoc_url=None)

    @property
    def app(self) -> FastAPI:
        return self.__app
