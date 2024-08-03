from fastapi import FastAPI


def app_factory() -> FastAPI:
    """Function for create and configure FaspApi app"""
    app = FastAPI(root_path="/api/v1")

    return app
