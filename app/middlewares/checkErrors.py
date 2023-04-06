from fastapi import Request, Response
from fastapi.responses import JSONResponse

from sqlalchemy.exc import OperationalError

async def checkErrors(request: Request, call_next):
    try:
        response = await call_next(request)
        return  response
    except OperationalError as E:
        return JSONResponse(content={"message":"Error establishing connection with database"},
                            status_code= 503)
    except Exception as E:
        return JSONResponse(content={"message":"Internal server error"}, status_code=500)
    