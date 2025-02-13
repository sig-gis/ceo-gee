from fastapi import FastAPI, Depends, Request
from fastapi.responses import JSONResponse
import traceback
from app.core.config import settings
from app.core.utils import initialize
from app.routes.gee import router as gee_router

app = FastAPI()

@app.on_event("startup")
def startup_event():
    initialize(ee_account=settings.gee_service_account, ee_key_path=settings.gee_private_key_path)

@app.middleware("http")
async def exception_handler_middleware(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        print(f"Unhandled Exception: {e}")
        traceback.print_exc()
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal Server Error"}
        )

app.include_router(gee_router)
