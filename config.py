from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

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

        self.__app.add_middleware(
            CORSMiddleware,
            allow_methods=['POST'],
            allow_origins=['*'],
            allow_credentials=True,
            allow_headers=['*']
        )

    @property
    def app(self) -> FastAPI:
        return self.__app


class GlobalArea(BaseModel):
    region: str
