from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from core.src.exceptions.business import (AlreadyExistsNameException,
                                          BusinessException,
                                          DateAlreadyExistsException)


def register_exception_handlers(app: FastAPI):
    @app.exception_handler(AlreadyExistsNameException)
    async def already_exists_name_exception_handler(
        request: Request, exc: AlreadyExistsNameException
    ):
        return JSONResponse(
            status_code=409,
            content={"message": exc.args[0]},
        )

    @app.exception_handler(BusinessException)
    async def general_exception_handler(request: Request, exc: BusinessException):
        print("efectivamente se llama a esta excetiopn")
        return JSONResponse(
            status_code=500,
            content={"message": exc.args[0]},
        )

    @app.exception_handler(DateAlreadyExistsException)
    async def date_already_exists_exception(
        request: Request, exc: DateAlreadyExistsException
    ):
        print("efectivamente se llama a esta excetiopn")
        return JSONResponse(
            status_code=409,
            content={"message": exc.args[0]},
        )
