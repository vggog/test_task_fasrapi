from fastapi import FastAPI

from .views import router


def app_factory() -> FastAPI:
    """Function for create and configure FaspApi app"""
    app = FastAPI(root_path="/api/v1")
    app.include_router(router)

    return app
