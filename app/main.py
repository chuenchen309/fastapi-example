import logging
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.utils.logger import logger
from app.config import configs as p
from app.api import router
from app.utils.logger import configure
from app.services.database.mongo import ConnectMongoDB

def conf_init():
    logger.debug(f'Start {p.APP_NAME} service...')

def configure_cors(app: FastAPI):
    origins = [p.APP_UI_URL, p.APP_API_URL, "localhost", "127.0.0.1"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

def create_app():
    logging.info("in create_app")
    configure()
    logging.info("in create_app, finish configure")

    app = FastAPI(
        title=f"{p.APP_NAME} Server",
        summary="Base on FastAPI Documentation ( https://fastapi.tiangolo.com ).",
        description=f"""
        APP_NAME::: {p.APP_NAME}
        APP_API_URL::: {p.APP_API_URL}
        version::: {p.APP_VERSION}
        """,
        version=f"{p.APP_VERSION}",
        servers=[{
            "url": p.APP_API_URL
        }])

    conf_init()
    configure_cors(app)
    app.include_router(router)

    ConnectMongoDB()

    return app
